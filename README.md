# Chebyshev [![Build Status](https://travis-ci.org/mlazaric/Chebyshev.svg?branch=master)](https://travis-ci.org/mlazaric/Chebyshev)

## Installation

```
pip install -r requirements.txt
```

## Functions

* [`exp(x)`](#expx)
* [`log(x + 1)`](#logx--1)
* [`sin(x)/x`](#sinxx)
* [`cos(x)`](#cosx)


## `exp(x)`

Coefficients for `exp(x)` on the `[0, 1]` interval:
     
|        Coefficient        |  Term  |
|---------------------------|--------|
| `+0.00228989065375017828` | `x**6` |
| `+0.00686967196125053310` | `x**5` |
| `+0.04293544975781583839` | `x**4` |
| `+0.16601707239688789919` | `x**3` |
| `+0.50019798967855455540` | `x**2` |
| `+0.99996662485953080601` | `x` |
| `+1.00000240440099563700` | `1` |


Maximum error on that interval is `2.724750259197606e-06`

![images/exp(x)_approximation.png](images/exp(x)_approximation.png)

![images/exp(x)_absolute_error.png](images/exp(x)_absolute_error.png)

## `log(x + 1)`

Coefficients for `log(x + 1)` on the `[0, 1]` interval:
     
|        Coefficient        |  Term  |
|---------------------------|--------|
| `-1.78206380208333333330` | `x**6` |
| `+1.68432617187500000000` | `x**5` |
| `+1.23596191406250000000` | `x**4` |
| `-0.76288859049479166667` | `x**3` |
| `-0.86048889160156250000` | `x**2` |
| `+1.16706848144531250000` | `x` |
| `+0.01269240000891307044` | `1` |


Maximum error on that interval is `0.026814743150641585`

![images/log(x_+_1)_approximation.png](images/log(x_+_1)_approximation.png)

![images/log(x_+_1)_absolute_error.png](images/log(x_+_1)_absolute_error.png)

## `sin(x)/x`

Coefficients for `sin(x)/x` on the `[-1, 1]` interval:
     
|        Coefficient        |  Term  |
|---------------------------|--------|
| `+0.00000269375975765659` | `x**8` |
| `-0.00019835866408658445` | `x**6` |
| `+0.00833331406945632250` | `x**4` |
| `-0.16666666426123592319` | `x**2` |
| `+0.99999999995192540491` | `1` |


Maximum error on that interval is `4.807454434541114e-11`

![images/sin(x)_x_approximation.png](images/sin(x)_x_approximation.png)

![images/sin(x)_x_absolute_error.png](images/sin(x)_x_absolute_error.png)

## `cos(x)`

Coefficients for `cos(x)` on the `[-1, 1]` interval:
     
|        Coefficient        |  Term  |
|---------------------------|--------|
| `+0.00002412120108317053` | `x**8` |
| `-0.00138829603431854838` | `x**6` |
| `+0.04166645537534185744` | `x**4` |
| `-0.49999997362171781040` | `x**2` |
| `+0.99999999947287565593` | `1` |


Maximum error on that interval is `5.271243441740125e-10`

![images/cos(x)_approximation.png](images/cos(x)_approximation.png)

![images/cos(x)_absolute_error.png](images/cos(x)_absolute_error.png)