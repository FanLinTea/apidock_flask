<template>
    <div style="width: 100%;height: 100%;overflow: hidden" @click="">
      <div style="height: 64px;width: 100%;background: #ffffff;box-shadow:3px 3px 5px 3px #e0e0e0;">
        <img src="../assets/logo.jpg" style="max-height: 34px;margin-top: 12px">
      </div>
      <div style="width: 100%;background: #ffffff;margin-top: 2px;height: 100%;">
        <div style="height: 30px"></div>
        <mu-button class="mu-button"
                   flat color="#ffffff"
                   textColor="#A2B5CD"
                   :class="{icon_bg:css===i.name}"
                   @click="click_but(i.name)"
                   v-for="i in routes"
                   :to="i.path">
          <mu-icon class="mu-icon" left :value=i.icon :class="{icon_bg:css===i.name}"></mu-icon>
          <P class="p" :class="{p2:css===i.name}">{{i.name}}</P>
        </mu-button>

      </div>

    </div>
</template>

<script>


export default {
    name: "LeftMenu",
    data() {
      return {
        css:'',
        routes:this.$router.options.routes[0].children,
      }
    },
  created() {
  },
    methods: {
      click_but(name, path) {
        this.css = name
      }
    },
}
</script>

<style scoped>

.mu-button {
  float:left;
  width: 100%;
  height: 66px;
}
.mu-icon {
  position: absolute;
  left: 14px;
  margin-right: 10px;
}
.p {
  font-size: 12px;
  position: absolute;
  left: 50px;
  margin: 0 0;
}
.p2{
  color: #1503EF;
}
.icon_bg {
  color: #1503EF;
  background: #eceff1;
}
</style>
