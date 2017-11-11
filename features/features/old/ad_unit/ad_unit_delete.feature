Feature: [3-6]AD Unit删除功能

#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_delete
  @ad_unit_delete_one
  Scenario: [3-6-1]删除单个AD Unit，删除成功！
	* 访问“AD Unit”页面：“http://m.mobvista.com/unit”
	
	* 选中要删除的“单个”AD Unit
	
	* 按下AD Unit的Delete按钮，弹出删除确认窗口
	
	* 按下删除AD Unit确认的OK按钮，删除选中的广告位
    
	* 删除AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_delete
  @ad_unit_cancel_delete
  Scenario: [3-6-2]删除单个AD Unit时，取消操作，取消删除成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 选中要删除的“单个”AD Unit
    
    * 按下AD Unit的Delete按钮，弹出删除确认窗口
    
    * 按下删除AD Unit确认的Cancel按钮，取消删除选中的广告位
    
    * AD Unit广告位删除取消成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_delete
  @ad_unit_delete_many
  Scenario: [3-6-3]删除多个AD Unit，删除成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 选中要删除的“多个”AD Unit
    
    * 按下AD Unit的Delete按钮，弹出删除确认窗口
    
    * 按下删除AD Unit确认的OK按钮，删除选中的广告位
    
    * 删除AD Unit广告位成功！
#-----------------------------------------------------------------------------------------------------------------------
  @ad_unit_delete
  @ad_unit_delete_cancel_many
  Scenario: [3-6-4]删除多个AD Unit时，取消操作，取消删除成功！
    * 访问“AD Unit”页面：“http://m.mobvista.com/unit”
    
    * 选中要删除的“多个”AD Unit
    
    * 按下AD Unit的Delete按钮，弹出删除确认窗口
    
    * 按下删除AD Unit确认的Cancel按钮，取消删除选中的广告位
    
    * AD Unit广告位删除取消成功！
    
    
    
