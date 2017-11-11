Feature: [4-3]Offline API Offer暂停功能

#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @api_offer
  @api_offer_paused
  @api_offer_paused_one
  Scenario: [4-3-1]暂停单个Offline API Offer，暂停成功！
  	* 操作API Offer前数据准备操作
  
	* 访问“Offline API Offer”页面：“http://m.mobvista.com/offer”
	
	* 选中要暂停的“单个”Offline API Offer
    
	* 按下Offline API Offer的Paused按钮
	
	* 按下Offline API Offer暂停确认的OK按钮
	
	* 暂停Offline API Offer成功！
	
	* 操作API Offer后数据清理操作
#-----------------------------------------------------------------------------------------------------------------------
  @finish
  @api_offer
  @api_offer_paused
  @api_offer_paused_many
  Scenario: [4-3-2]暂停多个Offline API Offer，暂停成功！
  	* 操作API Offer前数据准备操作
  
    * 访问“Offline API Offer”页面：“http://m.mobvista.com/offer”
    
    * 选中要暂停的“多个”Offline API Offer
    
    * 按下Offline API Offer的Paused按钮
    
    * 按下Offline API Offer暂停确认的OK按钮
    
    * 暂停Offline API Offer成功！
    
    * 操作API Offer后数据清理操作
    
    
