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
      Given 创建APP，创建结果保存到APP_temp
      """
      {
        'data':{
            user_id : $__fun(get_user_info, 'id'),
            channel_name : $__fun(get_random_string, 8),
            platform : 1,
         }
        'return': 'APP_temp'
      }
      """

      Given 请求设置
      """
      {

      }
      """

      When 输入参数,验证消息体
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


