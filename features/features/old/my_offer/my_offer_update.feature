Feature: [6-3]修改My Offer功能

#-----------------------------------------------------------------------------------------------------------------------
  @my_offer_update
  Scenario: [6-3-1]Start一个My Offer
	* 访问“My Offer”页面：“http://m.mobvista.com/offer/me”
	
	* 选中要Start的“单个”My Offer
	
	* 按下My Offer的Start按钮，激活指定Offer
	
	* 激活My Offer成功！
#-----------------------------------------------------------------------------------------------------------------------
  @my_offer_update
  Scenario: [6-3-2]Pause一个My Offer
    * 访问“My Offer”页面：“http://m.mobvista.com/offer/me”
    
    * 选中要Pause的“单个”My Offer
    
    * 按下My Offer的Pause按钮，暂停指定Offer
    
    * 暂停My Offer成功！
#-----------------------------------------------------------------------------------------------------------------------
  @my_offer_update
  Scenario: [6-3-3]修改My Offer的Offer Name属性
    * 访问“My Offer”页面：“http://m.mobvista.com/offer/me”
    
    * 按下要修改的My Offer的Edit按钮：“1007046”
    
    * 输入My Offer新的Offer Name：“New Offer Name”
    
    * 按下My Offer的Next按钮，进入下一页
    
    * 按下My Offer的Save Button，保存My Offer
    
    * 修改My Offer成功！
    
    
