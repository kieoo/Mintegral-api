Feature: [3-3]AD Unit修改功能

#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_update
  @ad_unit_update_native_name
  Scenario: [3-3-1]修改Native类型的AD Unit的Name属性，修改成功！
	* 访问“AD Unit”页面：“http://m.mobvista.com/unit”
	
	* 按下ID为“424”的Native类型的AD Unit的AD Unit Name，弹出修改窗口
	
	* 输入AD Unit新的AD Unit Name：“UpdateNative17”
	
	* 按下AD Unit的Save按钮，保存修改
	
	* 修改AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_update
  @ad_unit_update_banner_name
  Scenario: [3-3-2]修改Banner类型的AD Unit的Name属性，修改成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下ID为“420”的Banner类型的AD Unit的AD Unit Name，弹出修改窗口
    
    * 输入AD Unit新的AD Unit Name：“UpdateBanner01”
    
    * 按下AD Unit的Save按钮，保存修改
    
    * 修改AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_update
  @ad_unit_update_banner_refresh
  Scenario: [3-3-3]修改Banner类型的AD Unit的Auto Refresh属性，修改成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下ID为“420”的Banner类型的AD Unit的AD Unit Name，弹出修改窗口
    
    * 选择AD Unit的Auto Refresh：“60s”
    
    * 按下AD Unit的Save按钮，保存修改
    
    * 修改AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_update
  @ad_unit_update_banner_template
  Scenario: [3-3-4]修改Banner类型的AD Unit的Template属性，修改成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下ID为“419”的Banner类型的AD Unit的AD Unit Name，弹出修改窗口
    
    * 选择AD Unit的Template：“Mutli-elements”
    
    * 按下AD Unit的Save按钮，保存修改
    
    * 修改AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_update
  @ad_unit_update_interstitial_name
  Scenario: [3-3-5]修改Interstitial类型的AD Unit的Name属性，修改成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下ID为“423”的Interstitial类型的AD Unit的AD Unit Name，弹出修改窗口
    
    * 输入AD Unit新的AD Unit Name：“UpdateInterstitial02”
    
    * 按下AD Unit的Save按钮，保存修改
    
    * 修改AD Unit广告位成功！    
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_update
  @ad_unit_update_interstitial_template
  Scenario: [3-3-6]修改Interstitial类型的AD Unit的Template属性
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下ID为“423”的Interstitial类型的AD Unit的AD Unit Name，弹出修改窗口
    
    * 选择AD Unit的Template：“Single Pic”
    
    * 按下AD Unit的Save按钮，保存修改
    
    * 修改AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_update
  @unfinish
  Scenario: [3-3-7]修改APP WALL类型的AD Unit的Name属性，修改成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下ID为“11”的APP WALL类型的AD Unit的AD Unit Name，弹出修改窗口
    
    * 输入AD Unit新的Name：“Single Pic”
    
    * 按下AD Unit的Save按钮，保存修改
    
    * 修改AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_update
  @unfinish
  Scenario: [3-3-8]修改APP WALL类型的AD Unit的Entrance Image属性，修改成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下ID为“11”的APP WALL类型的AD Unit的AD Unit Name，弹出修改窗口
    
    * 选择AD Unit的Entrance Image：“Default”
    
    * 按下AD Unit的Save按钮，保存修改
    
    * 修改AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_update
  @unfinish
  Scenario: [3-3-8]修改APP WALL类型的AD Unit的Entrance Image属性，修改成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下ID为“11”的APP WALL类型的AD Unit的AD Unit Name，弹出修改窗口
    
    * 选择AD Unit的Red Point Setting：“Off”
    
    * 按下AD Unit的Save按钮，保存修改
    
    * 修改AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_update
  @unfinish
  Scenario: [3-3-10]修改APP WALL类型的AD Unit的Red Point Interval属性，修改成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下ID为“11”的APP WALL类型的AD Unit的AD Unit Name，弹出修改窗口
    
    * 输入AD Unit新的Red Point Interval：“22”
    
    * 按下AD Unit的Save按钮，保存修改
    
    * 修改AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_update
  @unfinish
  Scenario: [3-3-11]修改Native类型的AD Unit的Name属性为空，修改失败！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下ID为“11”的APP WALL类型的AD Unit的AD Unit Name，弹出修改窗口
    
    * 输入AD Unit新的AD Unit Name：“ ”
    
    * 按下AD Unit的Save按钮，保存修改
    
    * 修改AD Unit广告位失败！    
    
    
    
    
    
    
    
