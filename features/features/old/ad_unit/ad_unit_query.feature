Feature: [3-2]AD Unit查询功能

#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @test_add_hehe
  Scenario: [3-2-1]按AD Unit ID维度查询AD Unit，查询成功！
  	* 操作AD Unit前数据准备操作
#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @ad_unit_query
  @ad_unit_query_by_id
  Scenario: [3-2-1]按AD Unit ID维度查询AD Unit，查询成功！
  	* 操作AD Unit前数据准备操作
  
	* 访问“AD Unit”页面：“http://m.mobvista.com/unit”
	
	* 输入AD Unit的ID：“473”
	
	* 按下AD Unit的Search按钮，查找指定的广告位
	
	* 查询AD Unit广告位成功！
	
	* 操作AD Unit后数据清理操作
#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @ad_unit_query
  @ad_unit_query_by_name
  Scenario: [3-2-2]按AD Unit Name维度查询AD Unit，查询成功！
  	* 操作AD Unit前数据准备操作
  
	* 访问“AD Unit”页面：“http://m.mobvista.com/unit”
	
	* 输入AD Unit的广告位名称：“TestUnitQuery200”
	
	* 按下AD Unit的Search按钮，查找指定的广告位
	
	* 查询AD Unit广告位成功！
	
	* 操作AD Unit后数据清理操作
#-----------------------------------------------------------------------------------------------------------------------
  @unfinish
  @ad_unit_query
  @ad_unit_query_by_name
  Scenario:　[3-2-3]按APP Name维度查询AD Unit，查询成功！ 
  	* 操作AD Unit前数据准备操作
  	
	* 访问“AD Unit”页面：“http://m.mobvista.com/unit”
	
	* 输入AD Unit的APP Name：“TestApp_Android200”
	
	* 按下AD Unit的Search按钮，查找指定的广告位
	
	* 查询AD Unit广告位成功！ 
	
	* 操作AD Unit后数据清理操作   

    
  
    
    