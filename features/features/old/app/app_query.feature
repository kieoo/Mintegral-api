Feature: [2-2]查询APP功能

#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @app_query
  @app_query_by_id
  Scenario: [2-2-1]按ID维度查询APP，查询成功！
  	* 操作App前数据准备操作
  
	* 访问“APP”页面：“http://m.mobvista.com/app”
	
	* 输入查询的APP ID：“1000000016”

	* 按下APP的Search按钮，查询APP
	
	* 查询APP成功！
	
	* 操作App后数据清理操作
#-----------------------------------------------------------------------------------------------------------------------
  @unfinish
  @app_query
  @app_query_by_name
  Scenario: [2-2-2]按Name维度查询APP，查询成功！
  	* 操作App前数据准备操作
  	
    * 访问“APP”页面：“http://m.mobvista.com/app”
    
    * 输入查询的APP Name：“TestAppAdd_iOS01”

    * 按下APP的Search按钮，查询APP
    
    * 查询APP成功！
    
    * 操作App后数据清理操作
#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @app_query
  @app_query_by_id_none
  Scenario: [2-2-3]按ID维度查询APP，APP不存在，查询失败！
  	* 查询不存在App前数据准备操作
  	
    * 访问“APP”页面：“http://m.mobvista.com/app”
    
    * 输入查询的APP ID：“1000000016”

    * 按下APP的Search按钮，查询APP
    
    * APP不存在，查询APP失败！
    
    * 查询不存在App后数据清理操作

#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @app_query
  @app_query_by_id_deleted
  Scenario: [2-2-4]按ID维度查询APP，APP已删除，查询失败！
  	* 查询已删除App前数据准备操作
  	
    * 访问“APP”页面：“http://m.mobvista.com/app”
    
    * 输入查询的APP ID：“1000000020”

    * 按下APP的Search按钮，查询APP
    
    * APP已删除，查询APP失败！
    
    * 查询已删除App后数据清理操作
    
    
    


