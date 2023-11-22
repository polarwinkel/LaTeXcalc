# LaTeXcalc

## What is this?

LaTeXcalc is a LaTeX-Calculation-library for python3.

This calculates a mathematical formula written as a LaTeX-string.
It can use a given value-dict for variables in the formula.
The return-value is int or float.

## Supported features

LaTeXcalc can handle the following LaTeX-operations:

- apply `+`, `-`, `*`, `/` operators and the `-` as algebraic sign
- multiplication and division first, then addition and subtraction
- power `^`
- brackets `()`, `[]` and `{}` (also with `\left(`..`\right)`)
- squareroot `\sqrt{}`
- trigonometric functions like `\sin` or `\arctan`
- exponential numbers linke `1e+12`
- `\log` and `e^`
- `\pi` or `pi` and `e` as default-values `math.pi` and `math.e`
- `\frac{}{}` (works as abbreviated `\frac 1 2` as well)

make sure you always use `*` (or `\cdot`), because `xy` != `x*y`, in that case xy would be a value!

## How to use

You can install this by using pip: `pip install latexcalc` or alternatively by including the folder `latexcalc` in your python3-project.

Then all you need to do is

```
import latexcalc

c = latexcalc.calc('\sqrt{3^2+4^2}')
# or with variables:
c = latexcalc.calc(\sqrt(a^2+b^2)', {'a':3,'b':4})
print(c) # 5
```

## Limitations

All testet cases work, but there might still be wrong calculations in
special cases, so test it for your needs!

## Something missing?

Feel free to submit an issue if you find a bug or if you think something important is missing.
In that case please add a Line for the `test.py` to show the desired operation!

## Alternatives

There are some other libraries out there doing similar things, but at time of writing I didn't find anything that fulfilled my needs (lightweight, working with variables, ...).
So depending on your requirements this or maybe something else might be the right choise, thank's for cheching this out!
