# new feature
# Tags: optional
    
Feature: hehave learn TEST
@template
Scenario: [1-1-1]template
  Given template
  """
    {

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
   Input:{
      # 参数化两种格式
      id : $__fun(get_save_info, 'app_temp_appid', 'id'), # 参数化
      test : ${app_temp_appid.id} # 参数化
    }
   Output:{

      }
    }
  """
  Then 输入参数xxx，验证返回
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

