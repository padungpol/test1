Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> product = ['apple','banana','mango']
>>> print(len(product))
3
>>> product.append('Durian')
>>> product
['apple', 'banana', 'mango', 'Durian']
>>> product.remove('banana')
>>> 
>>> product
['apple', 'mango', 'Durian']
>>> print(product[0])
apple
>>> product[1] = 'แอปเปิ้ล'
>>> product
['apple', 'แอปเปิ้ล', 'Durian']
>>> product.insert(1,'มะม่วง')
>>> product
['apple', 'มะม่วง', 'แอปเปิ้ล', 'Durian']
>>> for pd in product
SyntaxError: invalid syntax
>>> for pd in product:
	print(pd)

	
apple
มะม่วง
แอปเปิ้ล
Durian
>>> fot i in range(10)
SyntaxError: invalid syntax
>>> for i in range(10)
SyntaxError: invalid syntax
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(111):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
>>> for i in range(1,11):
	print(i)

	
1
2
3
4
5
6
7
8
9
10
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for i in [20,30,99]
SyntaxError: invalid syntax
>>> for i in [20,30,99]:
	print(i)

	
20
30
99
>>> position = (500,500)
>>> print(position)
(500, 500)
>>> position = (700,500)
>>> print(position)
(700, 500)
>>> print(position[1])
500
>>> x,y = (500,700]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> x,y = (500,700):
	
SyntaxError: invalid syntax
>>> x,y = (500,700)
>>> print(x)
500
>>> print(y)
700
>>> product = {'มะม่วง':'ป้าแช่ม','กล้วย':'ลุงเปี๊ยก','ส้ม':'ป้าโชกุน'}
>>> print(product['มะม่วง'])
ป้าแช่ม
>>> product = {'มะม่วง':['ป้าแช่ม','ป้าปารีณา'],'กล้วย':'ลุงเปี๊ยก','ส้ม':'ป้าโชกุน'}
>>> print(product['มะม่วง'])
['ป้าแช่ม', 'ป้าปารีณา']
>>> print(product['มะม่วง'][1])
ป้าปารีณา
>>> product = {'มะม่วง':['ป้าแช่ม','ป้าปารีณา'],'กล้วย':'ลุงเปี๊ยก','ส้ม':{'191':'ป้าโชกุน','199':'ลุงเอก'}}
>>> print(product['ส้ม']['191'])
ป้าโชกุน
>>> 