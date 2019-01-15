/*
$(document).ready(function(){
	$("aside a").attr("onclick","test()")
});

function test(){
	$("section").html('<div class="dialog"><p>ytw</br>hello</div>')
};
*/

String.prototype.format = function() {
    var values = arguments;
    return this.replace(/\{(\d+)\}/g, function(match, index) {
        if (values.length > index) {
            return values[index];
        } else {
            return "";
        }
    });
};

$(document).ready(function() {
    //加载导航
    catalog_load()
    //添加导航click事件
    //$("aside ul li a").attr("onclick","a_click()")
});

function like_click(catid, sentenceid, userid) {

    console.log(catid, sentenceid, userid);
    $.ajax({
        type: "post",
        url: "/like",
        data: JSON.stringify({ 'catid': catid, 'sentenceid': sentenceid, 'userid': userid }),
        contentType: "application/json",
        datatype: "text",
        success: function(data) {
            console.log(data);
            $("span[id="+catid+"_"+sentenceid+"]").text("("+data+")")
        }, 
        error: function(jqXHR) {
            console.log("Error:" + jqXHR.status);
        }
    });
}

function favorite_click(catid, sentenceid, userid) {

    console.log(catid, sentenceid, userid);
    $.ajax({
        type: "post",
        url: "/favorite",
        data: JSON.stringify({ 'catid': catid, 'sentenceid': sentenceid, 'userid': userid }),
        contentType: "application/json",
        datatype: "text",
        success: function(data) {
            console.log(data);
            $("i[id=favorite_"+catid+"_"+sentenceid+"]").removeClass("favorite_on")
            $("i[id=favorite_"+catid+"_"+sentenceid+"]").removeClass("favorite_off")
            if (data==0) {
                 $("i[id=favorite_"+catid+"_"+sentenceid+"]").addClass("favorite_off")
            } else {
                $("i[id=favorite_"+catid+"_"+sentenceid+"]").addClass("favorite_on")
            }
        }, 
        error: function(jqXHR) {
            console.log("Error:" + jqXHR.status);
        }
    });
}

// 添加导航click时间
function a_click(s) {
    get_content(s)
}



//获取指定主题的内容列表
function get_content(catname) {
    $.ajax({
        type: "get",
        url: "/content?catname=" + catname + "&userid=admin",
        datatype: "json",
        success: function(data) {
            parsedJson = $.parseJSON(data);
            html = '<div id="content_list">'

            $.each(parsedJson, function(key, value) {
                html += '<div class="content">' +
                    '<h1>' + key + '</h1>';
                $.each(value, function(key, value) {
                    catid = value["catid"]
                    sentenceid = value["sentenceid"]
                    zh = value["zh"]
                    en = value["en"]
                    likeacount = value["likeacount"]
                    favorite = value["favorite"]
                    if (favorite==1) {
                        i_html='<i id="favorite_'+catid+'_'+sentenceid+'" class="fa fa-star fa-1x favorite_on" aria-hidden="true"></i>'
                    }
                   
                else {i_html='<i id="favorite_'+catid+'_'+sentenceid+'" class="fa fa-star fa-1x favorite_off" aria-hidden="true"></i>'
                  }

                    html += '<p>' + sentenceid + ':' + zh + '</p>' +
                            '<p>' + en + 
                            	// 点赞 or 打卡
                            	'<a class="btn btn-danger like_button" href="#" onclick="like_click(' + catid + ',' + sentenceid + ',1);return false;">'+
                                //'<button class="like_button" onclick="like_click(' + catid + ',' + sentenceid + ',1)">'+
                                	'<i class="fa fa-thumbs-up fa-1x" aria-hidden="true"></i>'+
                                	'<span id='+catid+'_'+sentenceid +'>(' + likeacount + ')</span>' +
                                 '</a>'+
                                // '</button>' +
                                 // 收藏 
                                //'<button class="like_button" onclick="favorite_click(' + catid + ',' + sentenceid + ',1)">'+
                                '<a class="btn btn-danger like_button" href="#" onclick="favorite_click(' + catid + ',' + sentenceid + ',1)">'+
                                	i_html +
                                '</a>'+
                                 //'</button>' + 
                             '</p>'
                })
                html += "</div>"

            })
            html += "</div>"
            $("section").html(html)
        },
        error: function(jqXHR) {
            console.log("Error:" + jqXHR.status);
        }
    });
}


// 加载导航
function catalog_load() {
    $.ajax({
        type: "get",
        url: "/catalog",
        datatype: "json",
        success: function(data) {
            html = "<ul>";
            //data = unescape(data.replace(/\\u/g, '%u'));
            parsedJson = $.parseJSON(data);
            $.each(parsedJson.catalogs, function(index, value) {
                html = html + "<li><a href=\"#\" onclick=\"a_click('{0}');return false;\">{0}</a><li>".format(value);
                // console.log(value);
            });
            html = html + "</ul>"
            $("aside").html(html)
        },
        error: function(jqXHR) {
            console.log("Error:" + jqXHR.status);
        }

    })
}