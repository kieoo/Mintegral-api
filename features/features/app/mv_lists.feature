# Created by qyke at 2017-11-3
Feature: APP模块mv_lists接口 自动化测试
  # test api : /app/mv_lists
  """
  查询active的app列表

  Request Url: BASIC_REQUEST_URL + /app/mv_lists
  Method : POST
  HEADER: with access_token + publisher_id 已经在template加入

  """
#-----------------------------------------------
  @test
  Scenario: 测试参数，app_id
    # Enter steps here
      Given 创建APP,保存到APP.tmp
      """
      {
        user_id :
        channel_name :
        platform :
        direct_market =
        url =
        icon =
        primary_category =
        secondary_category =
        grade =
        description =
        custom =
        timestamp =
        date =
        api =
        status =
        devinfo_encrypt =
        proportion =
        plct =
        plctb =
        postback = Column(String)
        exclude_package = Column(String)
        exclude_advertiser = Column(String)
        campaign_fields = Column(String)
        mtime = Column(Integer)
        admin_user_id = Column(Integer)
      }
      """

      Given 请求设置
      """
      {

      }
      """

      When 输入参数
      """
      {


        }
      """
      Then 验证消息体
      """
      {

        }
      """
      Then 检查MySql
      """
      {

        }
      """
      Then 检查mongo
      """
      {

        }
      """


