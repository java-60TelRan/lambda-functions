import json
import operator
import logging
from typing import Callable

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
OPERATIONS: dict = {
    '*': operator.mul,
    '-': operator.sub,
    '+': operator.add,
    '/': operator.truediv
}
def getOperandValue(calcData:dict, operandName:str) -> float:
    try:
        operand = float(calcData[operandName]["Value"])
    except KeyError:
        raise AttributeError(f"Missing {operandName}") 
    except ValueError:
        raise AttributeError(f"{operandName} should be a number")
    return operand
def getMessageAttributes(event)->dict:
    try:
        calcData: dict = event["Records"][0]["Sns"]["MessageAttributes"]
    except  KeyError:
        raise AttributeError("Wrong stricutre of SNS event") 
    return calcData  
def getOperation(calcData: dict) -> Callable[[float, float], float]:
    try:
        operation: dict = calcData["operation"]["Value"]
    except KeyError:
        raise AttributeError("No operation attribute") 
    res:  Callable[[float, float], float] = OPERATIONS.get(operation) 
    if not res:
        raise ValueError(f"Wrong operation {operation}")
    return res     
     
def lambda_handler(event, __):
    logger.debug(f"received event {event}")
    calcData: dict = getMessageAttributes(event)
    op1:float = getOperandValue(calcData, "op1")   
    op2:float = getOperandValue(calcData, "op2")
    print (getOperation(calcData)(op1, op2))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

