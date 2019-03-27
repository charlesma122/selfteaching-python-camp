'''
1.将数组[0,1,2,3,4,5,6,7,8,9]翻转
2.翻转后的数字拼接成字符串
3.用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
4.将获得的字符串进行翻转
5.将结果转为int类型
6.分别转换成二进制、八进制、十六进制
7.输出三种进制的结果
'''
a=[0,1,2,3,4,5,6,7,8,9]
a.reverse() #将数组翻转
print(a)

s = ''      #翻转后的数组拼接成字符串方法一
for i in range(0,10):  
    a[i]=str(a[i])
b=s.join(a)
print(b)


d=b[2:8]  #用切片方式取出第三到第八个字符
print(d)
c=int(d[::-1])  #将字符串进行反转，并转换为int类型
print(c)
print('二进制:',bin(c))    #转换成二进制、八进制、十六进制
print('八进制:',oct(c))
print('十六进制:',hex(c))
