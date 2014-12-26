---
layout: post
title: "通过jsonp解决浏览器跨域问题"
description: "讨论使用jsonp来解决跨域问题"
tags: [技术]
---

## 什么是jsonp

为了便于客户端使用数据，逐渐形成了一种非正式传输协议，人们把它称作JSONP，该协议的一个要点就是允许用户传递一个callback参数给服务端，然后服务端返回数据时会将这个callback参数作为函数名来包裹住JSON数据，这样客户端就可以随意定制自己的函数来自动处理返回数据了。

## 例子

### 客户端写法

这里借用了前端jquery框架对jsonp的支持

{% highlight JavaScript %}
var ajaxUrl = "http://192.168.8.141:9092/project/rest/team/matchResult/1/20/1/1000";
 
 
function localHandler(data) {
    console.log("fengshu")
    console.log(data);
}
 
var ajaxParam = {
    async: false,
    url: ajaxUrl, 
    type: "GET",
    dataType: 'jsonp',//非正式跨域传输协议
    jsonp: 'localHandler',
    success: function (json) {
        //回调数据在localHandler处理
    }
};
$.ajax(ajaxParam);
{% endhighlight %}

### 服务器端写法

{% highlight Java %}
@RequestMapping("/matchResult/{page}/{pageSize}/{type}/{matchId}")
public  void getMatchResult(HttpServletResponse response, @PathVariable("page") int page,
        @PathVariable("pageSize") int pageSize, @PathVariable("type") String type,@PathVariable("matchId") String matchId) {
    EntityList<MatchResult> datas = dddService.getTeamRanks(matchId,type,page,pageSize);
    ObjectMapper objectMapper = new ObjectMapper();
    String jsonResult=null;
    try {
        jsonResult = objectMapper.writeValueAsString(datas);
    } catch (JsonGenerationException e1) {
        e1.printStackTrace();
    } catch (JsonMappingException e1) {
        e1.printStackTrace();
    } catch (IOException e1) {
        e1.printStackTrace();
    }
    PrintWriter out=null;
    response.setCharacterEncoding("UTF-8");
    try {
        out = response.getWriter();
         
    } catch (IOException e) {
        e.printStackTrace();
    }  out.println( "localHandler("+jsonResult + ")");
            out.close();
}
{% endhighlight %}

## 总结

目前在浏览器端使用json传输数据jsonp传输协议是解决跨域问题的首选方案