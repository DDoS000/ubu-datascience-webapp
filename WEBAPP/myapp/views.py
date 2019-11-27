from django.shortcuts import render

# Create your views here.
def matmul(req):
    a = '12345\n67891'
    b = '12345\n67891\n98764'
    if req.method == 'POST':
        print('POST เด้อ')
        print(req.POST)
    else:
        print('GET เด้อ')
    return render(req, 'myapp/matmul.html',{
    'A':a,
    'B':b
    })
