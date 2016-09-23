//更新操作的弹窗提醒
function updateConfirm(){
    var optionNum = document.getElementById("optionvalue").selectedIndex;
    var optionValue = document.getElementById("optionvalue").options;
    var options = optionValue[optionNum].text
    var versionNum = document.getElementById("versionnum").value;
    console.log(options);
    console.log(versionNum);

    if (confirm("更新" + options + "的版本号为：" + versionNum + "?")){
        return true;
   }else{
        return false;
    }
}


//选服时的全选反选操作
$(function () {
    //全选或全不选
    $("#all").click(function(){
        if(this.checked){
            $("#list :checkbox").prop("checked", true);
        }else{
            $("#list :checkbox").prop("checked", false);
        }
     });
    //全选
    $("#selectAll").click(function () {
         $("#list :checkbox,#all").prop("checked", true);
    });
    //全不选
    $("#unSelect").click(function () {
         $("#list :checkbox,#all").prop("checked", false);
    });
    //反选
    $("#reverse").click(function () {
         $("#list :checkbox").each(function () {
              $(this).prop("checked", !$(this).prop("checked"));
         });
         allchk();
    });

    //设置全选复选框
    $("#list :checkbox").click(function(){
        allchk();
    });

    //获取选中选项的值
    $("#getValue").click(function(){
        var valArr = new Array;
        $('input[name="dbcheckbox"]:checked').each(function(i){
            valArr[i] = $(this).val();
        });
        var vals = valArr.join(',');
          alert(vals);
    });
});
function allchk(){
    var chknum = $("#list :checkbox").size();//选项总个数
    var chk = 0;
    $("#list :checkbox").each(function () {
        if($(this).prop("checked")==true){
            chk++;
        }
    });
    if(chknum==chk){//全选
        $("#all").prop("checked",true);
    }else{//不全选
        $("#all").prop("checked",false);
    }
}

//打游戏服补丁时的弹窗提醒
function patchConfirm(){
//    alert('dddddddddddd')
    var id_array=new Array();
    $('input[name="dbcheckbox"]:checked').each(function(){
        id_array.push($(this).val());//向数组中添加元素
    });
    var idstr=id_array.join(',');//将数组元素连接起来以构建一个字符串
//    alert(idstr);
    var fileName = document.getElementById("patchfile").innerHTML;
    var patchCmd = document.getElementById("cmdpatch").value

    if (confirm("执行：" + idstr + "服打" +fileName+"补丁操作？")){
        if (confirm("执行命令：/data/owinit/owServer 800* patch " + patchCmd + " /tmp/" + fileName )){
            return true;
        }else{
            return false;
            };

        return true;
   }else{
        return false;
    };
}


//打全球服补丁时的弹窗提醒
function patchGlobalConfirm(){
//    alert('dddddddddddd')
    var id_array=new Array();
    $('input[name="dbcheckbox"]:checked').each(function(){
        id_array.push($(this).val());//向数组中添加元素
    });
    var idstr=id_array.join(',');//将数组元素连接起来以构建一个字符串
//    alert(idstr);
    var fileName = document.getElementById("globalpatchfile").innerHTML;
    var patchCmd = document.getElementById("globalcmdpatch").value

    if (confirm("执行：" + "全球服_" + idstr + "服打" +fileName+"补丁操作？")){
        if (confirm("执行命令：/usr/owinit/globalServernew 800* patch " + patchCmd + " /tmp/" + fileName )){
            return true;
        }else{
            return false;
            };

        return true;
   }else{
        return false;
    };
}


//打跨服补丁时的弹窗提醒
function patchCrossConfirm(){
//    alert('dddddddddddd')
    var id_array=new Array();
    $('input[name="dbcheckbox"]:checked').each(function(){
        id_array.push($(this).val());//向数组中添加元素
    });
    var idstr=id_array.join(',');//将数组元素连接起来以构建一个字符串
//    alert(idstr);
    var fileName = document.getElementById("crosspatchfile").innerHTML;
    var patchCmd = document.getElementById("crosscmdpatch").value

    if (confirm("执行：" + "跨服_" + idstr + "服打" +fileName+"补丁操作？")){
        if (confirm("执行命令：/usr/owinit/owCross 800* patch " + patchCmd + " /tmp/" + fileName )){
            return true;
        }else{
            return false;
            };

        return true;
   }else{
        return false;
    };
}


