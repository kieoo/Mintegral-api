Feature: [2-3]修改APP功能

#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @app_update
  @app_update_name
  Scenario: [2-3-1]修改Android类型APP的APP Name属性，修改成功！
  	* 操作App前数据准备操作
  
	* 访问“APP”页面：“http://m.mobvista.com/app”
	
	* 按下ID为“1000000016”的APP的Edit按钮，弹出APP修改窗口
    
	* 输入APP的APP Name：“TestAppUpdate_Android01”

	* 按下APP的Save按钮，保存修改
	
	* 修改APP成功！
	
	* 操作App后数据清理操作
#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @app_update
  @app_update_direct_market
  Scenario: [2-3-2]修改Android类型APP的APK Offer Setting属性，修改成功！
  	* 操作App前数据准备操作
  	
    * 访问“APP”页面：“http://m.mobvista.com/app”
    
    * 按下ID为“1000000018”的APP的Edit按钮，弹出APP修改窗口
    
    * 选择APP的APK Offer Setting：“No Limit”
    
    * 按下APP的Save按钮，保存修改
    
    * 修改APP成功！
    
    * 操作App后数据清理操作
#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @app_update
  @app_update_ios_name
  Scenario: [2-3-3]修改iOS类型APP的APP Name属性，修改成功！
  	* 操作App前数据准备操作
  
    * 访问“APP”页面：“http://m.mobvista.com/app”
    
    * 按下ID为“1000000019”的APP的Edit按钮，弹出APP修改窗口
    
    * 输入APP的APP Name：“UpdateiOSAppName”
    
    * 按下APP的Save按钮，保存修改
    
    * 修改APP成功！
    
    * 操作App后数据清理操作


