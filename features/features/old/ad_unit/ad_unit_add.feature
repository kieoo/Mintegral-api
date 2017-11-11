Feature: [3-1]新增AD Unit功能

#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @ad_unit_add
  @ad_unit_add_banner
  Scenario: [3-1-1]新建一个Banner类型的AD Unit，新建成功！
	* 访问“AD Unit”页面：“http://m.mobvista.com/unit”
	
	* 按下Add AD Unit按钮，弹出新增广告位窗口
    
	* 输入AD Unit的AD Unit Name：“TestAddUnit201”
	
	* 选择AD Unit的APP：“TestApp_iOS2014”
	
	* 选择AD Unit的AD Format：“Banner”
	
	* 选择AD Unit的Auto Refresh：“30s”
	
	* 选择AD Unit的Template：“Single Pic”
	
	* 按下AD Unit的Save按钮，保存新建的广告位
	
	* 新增AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @ad_unit_add
  @ad_unit_add_interstitial
  Scenario: [3-1-2]新增一个Interstitial类型的AD Unit
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下Add AD Unit按钮，弹出新增广告位窗口
    
    * 输入AD Unit的AD Unit Name：“InterstitialUint02”
    
    * 选择AD Unit的APP：“TestApp_iOS2014”
    
    * 选择AD Unit的AD Format：“Interstitial”
    
    * 选择AD Unit的Orientation：“Horizontal Screen”
    
    * 选择AD Unit的Template：“Single Pic,Mutli-elements”
    
    * 按下AD Unit的Save按钮，保存新建的广告位
    
    * 新增AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @ad_unit_add
  @ad_unit_add_native
  Scenario: [3-1-3]新建一个Native类型的AD Unit，新建成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下Add AD Unit按钮，弹出新增广告位窗口
    
    * 输入AD Unit的AD Unit Name：“NativeUnit01”
    
    * 选择AD Unit的APP：“TestApp_iOS2014”
    
    * 选择AD Unit的AD Format：“Native”
    
    * 按下AD Unit的Save按钮，保存新建的广告位
    
    * 新增AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @unfinish
  @ad_unit_add
  @ad_unit_add_appwall
  Scenario: [3-1-4]新增一个APP WALL类型的AD Unit
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 按下Add AD Unit按钮，弹出新增广告位窗口
    
    * 输入AD Unit的AD Unit Name：“AppWallUnit01”
    
    * 选择AD Unit的APP：“TestApp_iOS2014”
    
    * 选择AD Unit的AD Format：“APP WALL”
    
    * 设置AD Unit的Entrance Image：“Default”
    
    * 选择AD Unit的Red Point Setting：“On”
    
    * 输入AD Unit的Red Point Interval：“23”
    
    * 按下AD Unit的Save按钮，保存新建的广告位
    
    * 新增AD Unit广告位成功！    
    
    
