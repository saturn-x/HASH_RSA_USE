$(document).ready(function(){
    $('#myhash').click(function(){
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
            url:"http://127.0.0.1:5000/vertify_hash", //自己url
            type:"post",
            data:{
                name:myname,
                description:mydescription
              },
            dataType:'json',
            success:function(data){
                // console.log(data)
                // var result=JSON.parse(data);
                console.log("请求成功");
                if(data.is==true){
                    console.log("hash验证通过");
                    alert("哈希验证通过，请上传密钥文件！")
                    $('#myname').attr("disabled","disabled");           
                    $('#mydescription').attr("disabled","disabled");
                    $('#myprocess').css({"width":"50%"});
                    $('#myhash').css({ "display": "none" });
                    $('#upload').css({ "display": "inline" });
                    $('#miyao').css({ "display": "inline" });
                }else{
                    alert("哈希验证失败，请填写正确信息！！！！")
                }
                console.log("请求完成");
      
            }
        })

        $('#upload').click(function(){
            var mymiyao=$("#mymiyao").val();
            $.ajax({
                url:"http://127.0.0.1:5000/vertify_rsa", //自己url
                type:"post",
                data:{
                    name:myname,
                    prikey:mymiyao
                  },
                dataType:'json',
                success:function(data){
                    // console.log(data)
                    // var result=JSON.parse(data);
                    console.log("请求成功");
                    if(data.is==true){
                        console.log("密钥验证通过");
                        alert("该商品真实存在！！")
                        $('#upload').text("验证完成");
                        $('#myprocess').css({"width":"100%"});
                        
                    }else{
                        alert("密钥验证失败，请填写正确信息！！！！")
                    }
                    console.log("请求完成");
          
                }
            
            })
        });





    });







});