# Created by qyke at 2017-11-3

@autoretry
Feature: APP模块mv_lists接口 自动化测试
"""
# TAG:  Feature or Scenario/ScenarioOutline with @autoretry
# NOTE: If you tag the feature, all its scenarios are retried.
"""

  # test api : /app/mv_lists
  """
  查询active的app列表

  Request Url: BASIC_REQUEST_URL + /app/mv_lists
  Method : POST
  HEADER: with access_token + publisher_id 已经在template加入

  READ MORE
    http://confluence.mobvista.com/pages/viewpage.action?title=Mobvista+Api+Document&spaceKey=~jiandong.wang
  """
#-----------------------------------------------
  @/app/mv_lists
  @finish
  Scenario: 测试参数，app_id存在，返回app信息
    # Enter steps here
      Given 创建随机app，结果保存到app_temp_appid
      """
      {
        'Data':{
            'user_id' : $__fun(get_user_info, 'id'),
            'channel_name' : 'mv_lists_test_appid',
            'platform' : 1,
         },
        'Save': 'app_temp_appid',
      }
      """

      When 输入参数app_id，验证返回不为空，且内容正确
      """
      {
        'Request_url': '/app/mv_lists',
        'Method' : 'POST',
        'Input':{
          'app_id': $__fun(get_save_info, 'app_temp_appid', 'id'),
        },

        'Output':{
            'code': 200,
            'data':{
              "limit":20,
              'total': 1,
              "page":1,
              "lists":[{
                'app_id' : $__fun(get_save_info, 'app_temp_appid', 'id'),
                'app_name' : 'mv_lists_test_appid',
                'platform' : 1,
                'ad_unit': 0,
              }]
            }
        }
      }
      """
#-----------------------------------------------
  @/app/mv_lists
  @finish
  Scenario: 测试参数，app_id不存在，返回app信息
    # Enter steps here
      Given 删除app
      """
      {
        'Data':{
            'id' : 99999,
         },
      }
      """

      When 输入参数app_id=99999，验证返回为空
      """
      {
        'Request_url': '/app/mv_lists',
        'Method' : 'POST',
        'Input':{
          'app_id': 99999,
        },

        'Output':{
            'code': 200,
            'data':{
              "limit":20,
              'total': 0,
              "page":1,
              "lists":[]
            }
        }
      }
      """
#-----------------------------------------------
  @/app/mv_lists
  @finish
  Scenario: 测试参数，app_id不合法，返回错误信息
    # Enter steps here
      Given 创建临时tmp_table，结果保存到temp_appid
      """
      {
        'Data':{
          'app_id':['test', 'test_9999', '1234_test']
        },
        'Save': 'temp_appid',
      }
      """

      When 输入参数app_id=99999，验证返回为空
      """
      {
        'Request_url': '/app/mv_lists',
        'Method' : 'POST',
        'Input':{
          'app_id': $__fun(get_save_info, 'temp_appid', 'app_id'),,
        },

        'Output':{
            'code': 200,
            'data':{
              "limit":20,
              'total': 0,
              "page":1,
              "lists":[]
            }
        }
      }
      """