<template>
    <div style="height: 100%;width: 100%;background: #fff">
        <!--左边Div-->
        <div style="width: 46%;float: left;height: 100%">
            <mu-appbar style="width: 100%;margin-top: 5px" color="#FFFFFF" z-depth="0" textColor="grey800" >
              <mu-button flat slot="left" style="margin-left: 100px">
                <img src="../assets/logo.jpg" style="max-width: 100px;">
              </mu-button>
            </mu-appbar>

            <mu-container>
              <mu-form ref="form" :model="validateForm" class="mu-demo-form">
                <mu-form-item label="用户名" help-text="账号由诸葛提供" prop="username" :rules="usernameRules">
                  <mu-text-field v-model="validateForm.username" prop="username"></mu-text-field>
                </mu-form-item>
                <mu-form-item label="密码" prop="password" :rules="passwordRules">
                    <mu-text-field type="password" v-model="validateForm.password" prop="password"></mu-text-field>
                </mu-form-item>
                <mu-form-item style="margin-top: 10px">
                  <mu-button color="#1503EF" @click="submit">提交</mu-button>
                  <mu-button @click="clear">重置</mu-button>
                </mu-form-item>
              </mu-form>
            </mu-container>
        </div>

        <!--右边div-->
        <div style="width: 54%;float: right;height: 100%;" id="bule">
            <div style="margin-top: 20px;margin-left:34%;overflow: hidden">
                <mu-button flat color="grey50" slot="right" class="mu_but">对接进度</mu-button>
                <mu-button flat color="grey50" slot="right" class="mu_but">api文档</mu-button>
                <mu-button flat color="grey50" slot="right" class="mu_but" style="border:1px solid white">Login</mu-button>
            </div>
        </div>


    </div>
</template>

<script>
  export default {
    name: "login",
    data() {
      return {
        usernameRules: [
          { validate: (val) => !!val, message: '必须填写用户名'},
          { validate: (val) => val.length >= 3, message: '用户名长度大于3'}
        ],
        passwordRules: [
          { validate: (val) => !!val, message: '必须填写密码'},
          { validate: (val) => val.length >= 3 && val.length <= 10, message: '密码长度大于3小于10'}
        ],
        validateForm: {
          username: '',
          password: '',
          isAgree: false
        }
      }
    },
     methods: {
        submit () {
          this.$refs.form.validate().then((result) => {
            console.log('form valid: ', result)
            this.$router.push({path:'/'})
          });
        },
        clear () {
          this.$refs.form.clear();
          this.validateForm = {
            username: '',
            password: '',
            isAgree: false
          };
        }
     }
  }

</script>

<style scoped>
  button{
    font-family: PingFang SC;
    /*font-weight: bolder;*/
  }
  #bule{
    background: linear-gradient(to top right, #1503EF, #283593, #f50057);
  }
  .mu-demo-form {
    width: 100%;
    max-width: 460px;
    margin: 30% auto;
  }
  .mu_but {
    text-transform:Capitalize;
  }
</style>
