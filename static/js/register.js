// 定义获取验证码按钮 的点击事件函数
function bindGetEmailCodeClick(){
// 定义获取验证码按钮 的点击事件
  $(".btn_get").click(function(event){
    // $this: 代表当前按钮的jQuery对象 将按钮定义为jQuery对象
    var $this = $(this);
    // 阻止默认事件 因为表单里的按钮有可能会自动提交表单, 此按钮为获取验证码 所以取消
    event.preventDefault();
    // 获取邮箱输入框的值
    var email = $("#inp_email").val();
    console.log(email);
    // 定义ajax请求 这里的$符号代表jQuery本身
    $.ajax({
      url: "/auth/verify/email?email=" + email,
      method: "GET",
      success: function(result){
        console.log(result);
        var code = result['code'];
        if (code == 200){
          // 重复点击倒计时
          var countdown = 5;
          // 取消点击事件
          $this.off("click");
          // 计时器函数 setInterval() 一个参数为要运行的函数, 另一个为超时时间(毫秒)
          var timer = setInterval(function(){
            $this.text("请在" + countdown + "秒后重试");
            countdown -=1 ;
            if (countdown == 0){
              // 清除定时器
              clearInterval(timer);
              // 按钮文字改回默认
              $this.text("获取验证码");
              // 重新绑定点击事件
              bindGetEmailCodeClick();
            }
            }, 1000
          );
          alert("验证码发送成功");
        }else{
          alert(result['msg'])
        }
      },
      fail: function (error){
        console.log(error);
      }
    })
    // $("input[name='email']")


  })

}

// $(): 浏览器加载完成后才执行(因为js在验证码之前加载, 所以需要等待下面的验证码按钮出来后才执行此事件)
$(function (){
  // 执行获取验证码函数
  bindGetEmailCodeClick();
})
