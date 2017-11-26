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
  @test
  Scenario: 测试参数，app_id存在，返回app信息
    # Enter steps here
      Given 准备MYSQL数据:创建随机两个app，结果保存到app_temp
      """
      {
        'Model': 'App',
        'app_temp1':{
                'user_id': $__fun(get_user_info, 'id'),
                'channel_name': $__fun(get_random_string, 5),
                'platform' : 1,
        },
        'app_temp2':{
                'user_id': $__fun(get_user_info, 'id'),
                'channel_name': $__fun(get_random_string, 5),
                'platform' : 2,
        },
      }
      """

      When 输入参数app_id，验证返回不为空，且内容正确
      """
      {
        'Request_url': '/app/mv_lists',
        'Method' : 'POST',
        'Input':{
          'app_id': $__fun(get_save_info, 'app_temp1', 'id'),
        },

        'Output':{
            'code': 200,
            'data':{
              "limit":20,
              'total': 1,
              "page":1,
              "lists":[{
                'app_id' : $__fun(get_save_info, 'app_temp1', 'id'),
                'app_name' :  $__fun(get_save_info, 'app_temp', 'channel_name'),
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
      Given 准备数据:删除app
      """
      {
        'Model': 'App',
        'Data1':{
                'id': 99999,
        },
        'Data2':{
                'id': 99998,
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
  Scenario: 测试参数，app_id不合法，返回错误信息
    # Enter steps here
      Given 准备数据:创建app_id列表
      """
      {
        'Data':{
          'app_id':['test', 'test_9999', '1234_test']
        }
      }
      """

      When 输入参数app_id=${tmp_table.app_id}，验证返回为空 X3
      """
      {
        'Request_url': '/app/mv_lists',
        'Method' : 'POST',
        'Input':{
          'user' : $__fun(get_user_info, 'id'),
          'tset' : $__fun(get_random_string, 5),
          'app_id': ${app_id},
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