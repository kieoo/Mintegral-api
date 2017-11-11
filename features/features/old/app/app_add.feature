Feature: [2-1]新增APP功能

#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @app_add
  @app_add_android
  Scenario:  [2-1-1]新建一个No APK的Android类型的APP，新建成功！
  	* 新增App前数据准备操作
  
	* 访问“APP”页面：“http://m.mobvista.com/app”
	
	* 按下Add APP按钮，弹出新增APP窗口
    
	* 输入APP的APP Name：“TestAppAdd_Android02”

	* 选择APP的Platform：“Android”
	
	* 选择APP的APK Offer Setting：“No APK”
	
	* 按下APP的Save按钮，保存新增的APP
	
	* 新增APP成功！
	
	* 新增App后数据清理操作
#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @app_add
  @app_add_iOS
  Scenario:  [2-1-2]新建一个iOS类型的APP，新建成功！
  	* 新增App前数据准备操作
  
    * 访问“APP”页面：“http://m.mobvista.com/app”
    
    * 按下Add APP按钮，弹出新增APP窗口
    
    * 输入APP的APP Name：“TestAppAdd_iOS02”

    * 选择APP的Platform：“iOS”
    
    * 按下APP的Save按钮，保存新增的APP
    
    * 新增APP成功！
    
    * 新增App后数据清理操作
 
