### 백준 R 풀이 설명
### https://www.acmicpc.net/help/language#language-72

### 백준 00단계 ___
### 00000번 _________
### _________설명_________

# print() 함수는 하나의 숫자 또는 문자를 출력
print("Hello World!")

# cat() 함수는 여러 숫자 또는 문자를 출력
cat("Hello World!")

# R Studio 환경 초기화
rm(list=ls())

# setwd("D:/Works/Programming/R/CodingSkillTest_R")

# 정수 입력 받는 방법
fp=file("stdin", "r")
n = scan(file=fp, what=integer(0), n=1)
# ?scan
# file: the name of a file to read data values from.
# what: the type of data to be read. 
#       The supported types are logical, integer, numeric, complex, 
#       character, raw and list.
# n: the maximum number of data values to be read,
#    Invalid values will be ignored.