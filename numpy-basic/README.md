# Numpy basic
> Numpy problem-solving study for Data Analysis



## Introduction

> 본 directory 학습내용의 출처는 [FutureSkill](https://futureskill.io/)의 [Contents](https://futureskill.io/content/79eba49a-178d-41be-8f88-137a5127742d)입니다.

**Numpy** 는 NUMerical PYthon 의 약자로서, 행렬 등을 다루기 위한 배열(Array)같은 형태의 자료형을 자유자재로 잘 다룰 수 있도록 도와주는 라이브러리이다.

데이터 분석을 하기 위해서는 데이터 연산을 해야 한다. 이 때 연산을 효율적으로 하기 위해서 데이터는 모두 벡터로 표현된다. 이런 벡터 연산에 최적화된 Numpy를 통해서 데이터를 빠르게 처리할 수 있다.



## Contents



1. creation
2. creation (2)
3. creation (3)
4. creation (4)
5. creation (5)
6. array data type
7. array data type (2)
8. indexing
9. indexing (2)
10. fancy indexing
11. array masking
12. max min
13. max min indexing
14. concat
15. concat (2)
16. vector
17. vector (2)
18. broadcasting
19. broadcasting (2)
20. reshaping
21. reshaping (2)
22. math function
23. math function (2)
24. math function (3)
25. sorting
26. sorting (2)
27. sorting (3)
28. sorting (4)



## Numpy Data type

> **reference** [Numpy documentation](https://numpy.org/devdocs/user/basics.types.html#array-types-and-conversions-between-types)

`numpy.bool` : `bool` Boolean (True or False) stored as a byte

`numpy.byte` : `signed char` Platform-defined

`numpy.ubyte` : `unsigned char` Platform-defined

`numpy.short` : `short` Platform-defined

`numpy.ushort` : `unsigned short` Platform-defined

`numpy.intc` : `int` Platform-defined

`numpy.uintc` : `unsigned int` Platform-defined

`numpy.int_` : `long` Platform-defined

`numpy.uint` : `unsigned long` Platform-defined

`numpy.longlong` : `long long` Platform-defined

`numpy.ulonglong` : `unsigned long long` Platform-defined

`numpy.half` / `numpy.float16` : Half precision float: sign bit, 5 bits exponent, 10 bits mantissa

`numpy.single` : `float` Platform-defined single precision float: typically sign bit, 8 bits exponent, 23 bits mantissa

`numpy.double` : `double` Platform-defined double precision float: typically sign bit, 11 bits exponent, 52 bits mantissa.

`numpy.longdouble` : `long double` Platform-defined extended-precision float

`numpy.csingle` : `float complex` Complex number, represented by two single-precision floats (real and imaginary components)

`numpy.cdouble` : `double complex` Complex number, represented by two double-precision floats (real and imaginary components)

`numpy.clongdouble` : `long double complex` Complex number, represented by two extended-precision floats (real and imaginary components).  



> **reference** [FutureSkill 김용담 creator](https://futureskill.io/content/79eba49a-178d-41be-8f88-137a5127742d/question/ced42779-2980-46d6-90a5-8d4d2f1e6c61)



platform에 따라 달라지는 data type을 제외하면 다음과 같다.

1. **Integer** 계열

   - `int8`, `int16`, `int32`, `int64`  
     모두 Integer를 나타내며 뒤에 따라오는 숫자에 따라 표현 범위가 정해짐.  

     > e.g. `int8`(8bytes) : -128 ~ 127

   - `uint8`, `uint16`, `uint32`, `uint64`    
     모두 unsigned integer를 나타내며 뒤에 따라오는 숫자에 따라 표현 범위가 정해짐.  

     > e.g. `uint16`(16bytes) : 0 ~ 65535



2. **Floating-point** 계열

   - `float32`, `float64`  
     모두 fixed-floating 타입을 나타내며 뒤에 따라오는 숫자에 따라 표현 범위가 정해짐.  
     (float16도 있으나, platform-dependent)  

     > e.g. `float32`(single precision, sign bit + 8 bits exponent + 23 bits mantissa)







---



#### Contents

- [Future Skill](https://futureskill.io/)

#### Course
- [[Python Data Analysis & Image Processing] - Dongbin Na](https://www.youtube.com/playlist?list=PLRx0vPvlEmdBx9X5xSgcEk4CEbzEiws8C)

#### Editor
- [**Colab**](https://colab.research.google.com/) / PyCharm
