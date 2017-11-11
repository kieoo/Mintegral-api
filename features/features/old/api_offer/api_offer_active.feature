Feature: [4-2]Offline API Offer激活功能

#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @api_offer
  @api_offer_active
  @api_offer_active_one
  Scenario: [4-2-1]激活单个Offline API Offer，激活成功！
  	* 操作API Offer前数据准备操作
  
	* 访问“Offline API Offer”页面：“http://m.mobvista.com/offer”
	
	* 选中要激活的“单个”Offline API Offer
    
	* 按下Offline API Offer的Start按钮
	
	* 按下Offline API Offer激活确认的OK按钮
	
	* 激活Offline API Offer成功！
	
	* 操作API Offer后数据清理操作
#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @api_offer
  @api_offer_active
  @api_offer_active_many
  Scenario: [4-2-2]激活多个Offline API Offer
  	* 操作API Offer前数据准备操作
  	
    * 访问“Offline API Offer”页面：“http://m.mobvista.com/offer”
    
    * 选中要激活的“多个”Offline API Offer
    
    * 按下Offline API Offer的Start按钮
    
    * 按下Offline API Offer激活确认的OK按钮
    
    * 激活Offline API Offer成功！
    
    * 操作API Offer后数据清理操作
    
    
