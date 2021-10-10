$(document).ready(function(){
    prikey='';
    fileName='';
    console.log("加载完成！");
    $("#mysubmit").click(function(){
            var myname=$("#myname").val();
            fileName=myname+'.txt';
            var mydescription=$("#mydescription").val();
            if(myname==''||mydescription==''){
                alert("请正确填写商品信息");
                return;
            }
            console.log(myname+" "+mydescription);
            console.log("发送商品添加请求");
            $.ajax({
                url:"http://127.0.0.1:5000/add_object", //自己url
                type:"post",
                data:{
                    name:myname,
                    description:mydescription
                  },
                dataType:'json',
                success:function(data){
                    console.log(data);
                    if(data.isexist=="true"){
                        alert("该物品名称已经存在，请重新输入！！！");
                        return;
                    }
                    // console.log(data)
                    // var result=JSON.parse(data);
                    console.log("请求成功");
                    console.log(data.sk);
                    prikey=data.sk;
                    console.log("请求完成");
                    $('#myname').attr("disabled","disabled");           
                    $('#mydescription').attr("disabled","disabled");
                    $('#mysubmit').css({ "display": "none" });
                    $('#download').css({ "display": "inline" });
                }
            })
    });

    $('#download').click(function(){
        alert("正在下载私钥····")
        let blob = new Blob([prikey], {
            type: "text/plain;charset=utf-8"
        });
        let reader = new FileReader();
        reader.readAsDataURL(blob);
        reader.onload = function(e) {
            let a = document.createElement('a');
            a.download = fileName;
            a.href = e.target.result;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }
    })
});
