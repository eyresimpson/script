// ==UserScript==
// @name         隐藏按钮
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  临时应用
// @match        *://*/*
// @grant        GM_addStyle
// ==/UserScript==

(function() {
    'use strict';

    // 要隐藏的类名
    var className = "van-button--info";

    // 通过GM_addStyle函数添加样式（通过display: none隐藏元素）
    GM_addStyle("." + className + " { display: none !important; }");

    // 到下面网址即可查看效果，其中的info类型的按钮会被隐藏
    // https://vant-contrib.gitee.io/vant/v2/#/en-US/button

})();