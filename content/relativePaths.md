Title: Relative Paths
Date: 2019-05-27
Modified: 2019-05-27
Category: Posts
Tags: Python, Coding
Slug: Relative Paths in VSCode on Windows
Author: Alex Mendiola
Summary: Issues with relative paths in VSCode on Windows.

As I continue through the Python for Developers course offered by Mosh Hamedani, I noticed some odd behavior in Visual Studio Code. The relative paths that Mosh was describing returned an error in my code. At first, I solved the issue by creating a raw string. For instance,

```python
Path("ecommerce")
```
didn't work so I copied the full path and used the raw string.

```python
Path(r"C:\Users\rig\coding\python\codeEnv\Mosh\ecommerce")
```
I realized later that I could use the relative path but I had to include the parent directory displayed in the file tab in Visual Studio Code. In my case...

```python
Path("Mosh\ecommerce")
```
worked just fine.

So, if you're using Windows and Visual Studio Code, be sure to include any parent directories in the file tab when writing relative paths in Visual Studio.