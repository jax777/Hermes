webpackJsonp([1],{"1wM8":function(t,n){},"2Ktn":function(t,n){},"3ay9":function(t,n){},"5TrB":function(t,n){},"5woi":function(t,n){},DE5D:function(t,n,e){"use strict";n.a={data:function(){return{tableData:[{hash:"",domain:"",http:"",dns:""}],form:{name:"",passwd:""},reqlog:"log info",dialogFormlogin:!1,mydomain:"sub domain"}},methods:{showHttp:function(t){var n=this;console.log(t),this.dialogFormlogin=!0,this.axios.get("/showHttp/"+t).then(function(t){n.reqlog=t.data})},showDns:function(t){var n=this;console.log(t),this.axios.get("/showDns/"+t).then(function(t){n.reqlog=t.data})},getDomain:function(){var t=this;this.axios.get("/getDomain").then(function(n){t.reqlog=n.data})},showDomains:function(){console.log("写domain"),this.tableData=[{hash:"hashdomain",domain:"2016-05-02",http:"1",dns:"1"},{hash:"hashdomain",domain:"2016-05-03",http:"2",dns:"2"}]},handleDelete:function(t,n){console.log("哈哈哈 没写 不写了")},login:function(t,n){this.axios.post("/login",{name:t,passwd:n}).then(function(t){"success"===t&&this.showDomains()}),console.log(t)},loout:function(){var t=new Date;t.setTime(t.getTime()-1),document.cookie="prefix= 1;expires="+t.toGMTString()}}}},HB7i:function(t,n){},I4t6:function(t,n,e){"use strict";n.a={data:function(){return{logining:!1,form:{mail:"",passwd:""},checked:!0}},methods:{login:function(t,n){this.axios.post("/login",{mail:t,passwd:n}).then(function(t){"1"===t.data?location.href="#/info":(alert(t.data),console.log(t.data))})}}}},IGat:function(t,n){},K31e:function(t,n,e){"use strict";var a=e("I4t6"),o=e("W+lU"),s=e("VU/8"),i=s(a.a,o.a,null,null,null);n.a=i.exports},M93x:function(t,n,e){"use strict";function a(t){e("1wM8")}var o=e("xJD8"),s=e("ovHA"),i=e("VU/8"),l=a,r=i(o.a,s.a,l,null,null);n.a=r.exports},NHnr:function(t,n,e){"use strict";Object.defineProperty(n,"__esModule",{value:!0});var a=e("5TrB"),o=(e.n(a),e("HJMx")),s=e.n(o),i=e("3ay9"),l=(e.n(i),e("qubY")),r=e.n(l),u=e("Oxd1"),c=(e.n(u),e("Mezo")),f=e.n(c),d=e("qKch"),m=(e.n(d),e("vqwl")),p=e.n(m),h=e("2Ktn"),v=(e.n(h),e("q4le")),g=e.n(v),w=e("5woi"),_=(e.n(w),e("orbS")),b=e.n(_),y=e("HB7i"),x=(e.n(y),e("mtrD")),D=e.n(x),k=e("IGat"),H=(e.n(k),e("psK2")),q=(e.n(H),e("LR6y")),M=e.n(q),K=e("7+uW"),E=e("YaEn"),R=e("M93x"),O=e("mtWM"),S=e.n(O),T=e("Rf8U"),U=e.n(T);K.default.config.productionTip=!0,S.a.defaults.withCredentials=!0,K.default.use(U.a,S.a),K.default.use(M.a),K.default.use(D.a),K.default.use(b.a),K.default.use(g.a),K.default.use(p.a),K.default.use(f.a),K.default.use(r.a),K.default.use(s.a),new K.default({el:"#app",router:E.a,template:"<App/>",components:{App:R.a}})},Oxd1:function(t,n){},"W+lU":function(t,n,e){"use strict";var a=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("el-form",{ref:"form",attrs:{model:t.form,"label-width":"80px"}},[e("el-form-item",{attrs:{label:"用户名"}},[e("el-input",{model:{value:t.form.mail,callback:function(n){t.form.mail=n},expression:"form.mail"}})],1),t._v(" "),e("el-form-item",{attrs:{label:"密码"}},[e("el-input",{model:{value:t.form.passwd,callback:function(n){t.form.passwd=n},expression:"form.passwd"}})],1),t._v(" "),e("el-form-item",[e("el-button",{attrs:{type:"primary"},on:{click:function(n){t.login(t.form.mail,t.form.passwd)}}},[t._v("登陆")])],1)],1)},o=[],s={render:a,staticRenderFns:o};n.a=s},"Y/HG":function(t,n,e){"use strict";var a=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("div",[e("el-tag",{attrs:{type:"primary"}},[t._v(t._s(t.mydomain))]),t._v(" "),e("el-button",{attrs:{type:"primary"}},[t._v("修改密码")]),t._v(" "),e("el-button",{attrs:{type:"primary"}},[t._v("清空记录")]),t._v(" "),e("el-button",{attrs:{type:"primary"},nativeOn:{click:function(n){t.logout(n)}}},[t._v("退出")]),t._v(" "),e("el-table",{staticStyle:{width:"100%"},attrs:{data:t.tableData}},[e("el-table-column",{attrs:{prop:"domain",label:"domain"}}),t._v(" "),e("el-table-column",{attrs:{prop:"http",label:"http"},scopedSlots:t._u([{key:"default",fn:function(n){return[e("el-button",{attrs:{size:"large"},on:{click:function(e){t.showHttp(n.row.hash)}}},[t._v(t._s("http："+n.row.http))]),t._v(" "),e("el-button",{attrs:{size:"small",type:"danger"},on:{click:function(e){t.handleDelete(0,n.hash)}}},[t._v("删除")])]}}])}),t._v(" "),e("el-table-column",{attrs:{prop:"dns",label:"dns"},scopedSlots:t._u([{key:"default",fn:function(n){return[e("el-button",{attrs:{size:"large"},on:{click:function(e){t.showDns(n.row.hash)}}},[t._v(t._s("dns："+n.row.dns))]),t._v(" "),e("el-button",{attrs:{size:"small",type:"danger"},on:{click:function(e){t.handleDelete(1,n.hash)}}},[t._v("删除")])]}}])})],1),t._v(" "),e("textarea",{staticStyle:{width:"100%","overflow-x":"hidden","overflow-y":"auto"},attrs:{rows:"25",cols:"80",readonly:"readonly"}},[t._v(t._s(t.reqlog))])],1)},o=[],s={render:a,staticRenderFns:o};n.a=s},YaEn:function(t,n,e){"use strict";var a=e("7+uW"),o=e("/ocq"),s=e("nOR6"),i=e("K31e");a.default.use(o.a),n.a=new o.a({routes:[{path:"/login",name:"login",component:i.a},{path:"/info",name:"domains",component:s.a},{path:"/",name:"login",component:i.a}]})},nOR6:function(t,n,e){"use strict";var a=e("DE5D"),o=e("Y/HG"),s=e("VU/8"),i=s(a.a,o.a,null,null,null);n.a=i.exports},ovHA:function(t,n,e){"use strict";var a=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("div",{attrs:{id:"app"}},[e("router-view")],1)},o=[],s={render:a,staticRenderFns:o};n.a=s},psK2:function(t,n){},qKch:function(t,n){},xJD8:function(t,n,e){"use strict";n.a={name:"app"}}},["NHnr"]);
//# sourceMappingURL=app.3b435dc515e89e56e35e.js.map