<template>
    <div style="width: 100%;height: 100%;overflow: hidden" @click="">
      <div style="height: 60px;width: 100%;background: #ffffff;border-left: 2px solid #cfd8dc">
        <mu-chip class="demo-chip" color="teal" @delete="handleClose" delete style="margin-top: 12px">
          <mu-avatar :size="32" color="blue">
            <mu-icon value="face"></mu-icon>
          </mu-avatar>
          icon avatar chip
        </mu-chip>
      </div>
      <div style="width: 100%;background: #ffffff;margin-top: 2px;height: 100%">
          <mu-button class="mu-button"
                       flat color="#ffffff"
                       style="margin-top: 30px;"
                       textColor="#A2B5CD"
                       :class="{icon_bg:css===1}"
                       @click="click_but(1)">
              <mu-icon class="mu-icon" left value="grade" :class="{icon_bg:css===1}"></mu-icon>
              <P class="p" style="font-size: 12px" :class="{icon_bg:css===1}">Star</P>
            </mu-button>

            <mu-button class="mu-button" flat color="#ffffff" textColor="#A2B5CD" @click="click_but(2)" :class="{icon_bg:css===2}">
              <mu-icon class="mu-icon" left value="grade" :class="{icon_bg:css===2}"></mu-icon>
              <P class="p" style="font-size: 12px" :class="{icon_bg:css===2}">Star</P>
            </mu-button>
      </div>

    </div>
</template>

<script>
  export default {
      name: "RightMenu",
      data() {
        return {
          css:'',
        }
      },
      methods: {
        click_but(x) {
          this.css = x
        }
      },

  }
</script>

<style scoped>

.mu-button {
  float:left;
  width: 100%;
  height: 60px;
}
.mu-icon {
  margin-left: -36px;
}
.p {
  font-size: 12px
}
.icon_bg {
  color: #1503EF;
  background: #eceff1;
}
</style>
