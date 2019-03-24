# Examples 

Daft Punk album cover

![Daft Punk Ascii art](https://imgur.com/HrhgnSl.png)

The GitHub logo

![GitHub Logo Ascii art](https://imgur.com/GqbhjFN.png)

Demonstration of grayscale

>As Ascii art:

![Grayscale Ascii art](https://imgur.com/Z6SJ3yD.png)
>Original:

![Original grayscale image](https://imgur.com/Qd0I8Ty.png)
# How it works
1. Converts the image to grayscale
2. Resizes the image to have a width of 900px
3. Takes a group of 9x20 pixels 

>Equal to the dimensions of a single character in my case (Using Consolas, 16pt) 
4. Takes the average brightness
5. Matches the area to the letter whom's grayscale is the most similar

# Test it yourself
You need Python Pillow to run this script.
```pip install Pillow``` 

```
Convert.py -f "my/file/name.png"
```

# Arguments
-f
  >File to convert

-w
>	Width of output image in characters

-c
>	Add additional/Remove contrast [Default is 1, higher = more contrast]

-ea
>	Include extended ASCII range

-i
>	Inverts the image before converting

-b
>	Block certain characters from appearing in image
>	Example: python Convert.py -f "my/file.png" -b "&" "Q"


# Sidenotes
May not work as well with fonts other than Consolas

Images that have extreme ratios (like 50:1) may not work
