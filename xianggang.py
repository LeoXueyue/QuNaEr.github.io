import re
html="""
<div class="sight_item sight_itempos" mp-role="sightItem" data-id="2610530553" data-sight-name="香港机场快线" data-sight-category="交通" data-districts="香港·香港" data-point="113.946544,22.319128" data-foreign="false" data-children-count="0" data-sight-img-u-r-l="http://img1.qunarzz.com/sight/p0/201403/10/538327735b9ace87fb3cff96caf9285d.jpg_280x200_1cb65317.jpg" data-address="香港特别行政区" data-sale-count="10">
                        <div class="sight_item_detail clrfix"><span class="sight_item-topbg"></span>
                            <div class="sight_item_show">
                                <div class="show loading">
                                    <div class="imgshadow"></div>
                                    <a data-click-type="l_pic" href="/ticket/detail_2610530553.html?st=a3clM0QlRTclODMlQUQlRTklOTclQTglRTYlOTklQUYlRTclODIlQjklMjZpZCUzRDQxNDUyJTI2dHlwZSUzRDAlMjZpZHglM0Q4ODAlMjZxdCUzRGRlZmF1bHRUeXBlJTI2YXBrJTNEMiUyNnNjJTNEV1dXJTI2bHIlM0QlRTUlOEMlOTclRTQlQkElQUMlMjZmdCUzRCU3QiU3RA%3D%3D#from=mpl_search_suggest" target="_blank" hidefocus="true" title="香港机场快线"><img data-original="http://img1.qunarzz.com/sight/p0/201403/10/538327735b9ace87fb3cff96caf9285d.jpg_280x200_1cb65317.jpg" alt="香港机场快线" class="img_opacity load" onerror="this.src='//simg1.qunarzz.com/piao/images/loading_camel_gray.gif'" src="http://img1.qunarzz.com/sight/p0/201403/10/538327735b9ace87fb3cff96caf9285d.jpg_280x200_1cb65317.jpg"></a>
                                </div>
                            </div>
                            <div class="sight_item_about"><h3 class="sight_item_caption"><a data-click-type="l_title" class="name" href="/ticket/detail_2610530553.html?st=a3clM0QlRTclODMlQUQlRTklOTclQTglRTYlOTklQUYlRTclODIlQjklMjZpZCUzRDQxNDUyJTI2dHlwZSUzRDAlMjZpZHglM0Q4ODAlMjZxdCUzRGRlZmF1bHRUeXBlJTI2YXBrJTNEMiUyNnNjJTNEV1dXJTI2bHIlM0QlRTUlOEMlOTclRTQlQkElQUMlMjZmdCUzRCU3QiU3RA%3D%3D#from=mpl_search_suggest" target="_blank" hidefocus="true" title="香港机场快线">香港机场快线</a>
                            </h3>
                                <div class="sight_item_info">
                                    <div class="clrfix"><span class="area">[<a href="/ticket/list_%E9%A6%99%E6%B8%AF%C2%B7%E9%A6%99%E6%B8%AF.html#from=mpl_search_suggest" target="_blank" hidefocus="true" title="香港·香港">香港·香港</a>]</span>
                                        <div class="sight_item_hot"><span class="product_star_level"><em title="热度: 0.0"><span style="width:0.0%;">热度 0.0</span></em></span><span class="sight_item_hot_text">热度：</span></div>
                                    </div>
                                    <p class="address color999"><span title="香港特别行政区">地址：香港特别行政区</span><a href="javascript:void(0)" hidefocus="true" class="map_address blue" data-sightid="2610530553">地图</a></p>
                                    <div class="intro color999" title="全球首屈一指的铁路系统">全球首屈一指的铁路系统</div>
                                </div>
                            </div>
                            <div class="sight_item_pop">
                                <table>
                                    <tbody><tr>
                                        <td><span class="sight_item_price"><i>¥</i><em>105</em>&nbsp;起</span></td>
                                    </tr>
                                    <tr>
                                        <td style="display: none"><span class="sight_item_discount">5.8折</span>&nbsp;&nbsp;&nbsp;<span class="sight_item_source">票面价：</span></td>
                                    </tr>
                                    <tr>
                                        <td><a data-click-type="l_title" class="sight_item_do" href="/ticket/detail_2610530553.html?st=a3clM0QlRTclODMlQUQlRTklOTclQTglRTYlOTklQUYlRTclODIlQjklMjZpZCUzRDQxNDUyJTI2dHlwZSUzRDAlMjZpZHglM0Q4ODAlMjZxdCUzRGRlZmF1bHRUeXBlJTI2YXBrJTNEMiUyNnNjJTNEV1dXJTI2bHIlM0QlRTUlOEMlOTclRTQlQkElQUMlMjZmdCUzRCU3QiU3RA%3D%3D#from=mpl_search_suggest" target="_blank" hidefocus="true" title="香港机场快线">查看景点&nbsp;<span>»</span></a>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="sight_item_sold-num">月销量：<span class="hot_num">10</span></td>
                                    </tr>
                                </tbody></table>
                            </div>
                            <div class="setbd"></div>
                        </div>
                    </div>
"""
sight_info_patterns = re.compile(
            r'<div.*?class="sight_item_show">.*?<div.*?class="show loading">.*?<a.*?>.*?<img.*?data-original="(.*?)".*?>.*?</a>.*?</div>.*?</div>.*?'
            r'<div.*?class="sight_item_about">.*?<a.*?class="name".*?>(.*?)</a>.*?'
            r'<div.*?class="sight_item_info">.*?<div.*?class="clrfix">.*?<span.*?class="area">.*?<a.*?>(.*?)</a>.*?</span>.*?'
            r'<div.*?class="sight_item_hot">.*?<span.*?>热度 (.*?)</span>.*?</div>.*?</div>.*?'
            r'<p.*?>.*?<span.*?>地址：(.*?)</span>.*?</p>.*?'
            r'<div.*?>(.*?)</div>.*?</div>.*?</div>.*?'
            r'<div.*?class="sight_item_pop">.*?<table>.*?'
            r'<span.*?class="sight_item_price">.*?<em>(.*?)</em>.*?</span>.*?'
            r'<td.*?class="sight_item_sold-num">月销量：<span.*?>(.*?)</span>.*?</td>.*?'
            r'</table>.*?</div>', re.S)
sight_item=re.findall(sight_info_patterns,html)
print(len(sight_item))
print(sight_item)