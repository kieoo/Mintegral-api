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
  # app_id,app_name
#-----------------------------------------------
  @/app/mv_lists
    @finish
  Scenario: 测试参数，app_id, app_name存在，返回app信息
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
                'app_name' :  $__fun(get_save_info, 'app_temp1', 'channel_name'),
                'platform' : 1,
                'ad_unit': 0,
              }]
            }
        }
      }
      """

      When 输入参数app_name，验证返回不为空，且内容正确
      """
        {
          'Request_url': '/app/mv_lists',
          'Method' : 'POST',
          'Input':{
            'app_name': ${app_temp2.channel_name},
          },

          'Output':{
              'code': 200,
              'data':{
                "limit":20,
                'total': 1,
                "page":1,
                "lists":[{
                  'app_id' : ${app_temp2.id},
                  'app_name' :  ${app_temp2.channel_name},
                  'platform' : 2,
                  'ad_unit': 0,
                }]
              }
          }
        }
      """
#-----------------------------------------------
  @/app/mv_lists
    @finish
  Scenario: 测试参数，app_id, app_name不存在，返回app信息为空
    # Enter steps here
      Given 准备MYSQL数据:删除app
      """
      {
        'Model': 'App',
        'delete1':{
                'user_id': $__fun(get_user_info, 'id'),
                'id': 99999,
        },
        'delete2':{
                'user_id': $__fun(get_user_info, 'id'),
                'channel_name': 'auto_test_app1',
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

      When 输入参数app_name=auto_test_app1，验证返回为空
      """
      {
        'Request_url': '/app/mv_lists',
        'Method' : 'POST',
        'Input':{
          'app_name': 'auto_test_app1',
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
  Scenario: 测试参数，app_id不合法，返回为空
    # Enter steps here
      Given 准备数据:创建app_id列表
      """
      {
        'Data':{
          'app_id':['test', 'test_9999', '1234_test']
        }
      }
      """

      When 输入参数app_id=${app_id}，验证返回为空 X3
      """
      {
        'Request_url': '/app/mv_lists',
        'Method' : 'POST',
        'Input':{
          'app_id': ${Tmp_Data.app_id},
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
  # unit_id, unit_name, unit_type
#-----------------------------------------------
  @/app/mv_lists
    @finish
  Scenario: 测试参数，unit_id存在，返回app下对应unit信息
    # Enter steps here
      Given 准备数据:创建app_id
      """
        {
          'Model': 'App',
          'app_temp1':{
                  'user_id': $__fun(get_user_info, 'id'),
                  'channel_name': $__fun(get_random_string, 5),
                  'platform' : 1,
          },
        }
      """
      Given 准备数据:创建unit
      """
        {
          'Model': 'unit',
          'unit_temp1':{
                  'user_id': $__fun(get_user_info, 'id'),
                  'channel_id' : ${app_temp1.id},
                  'channel_name': $__fun(get_random_string, 5),
                  'platform' : 1,
          },
        }
      """