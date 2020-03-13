<template>
  <div>
    <v-menu offset-y bottom left min-width="150px">
      <template v-slot:activator="{ on }">
        <v-btn icon v-on="on">
          <v-avatar color="primary" size="30">
            <span class="white--text">
              {{ usernameforAvatar() }}
            </span>
          </v-avatar>
        </v-btn>
      </template>
      <v-list dense class="py-1">
        <div v-for="(item, index) in items" :key="index">
          <v-list-item v-if="item.click" @click="item.click">
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
          <v-list-item v-else-if="item.title">
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
          <v-divider v-if="item.divider" />
        </div>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
export default {
  name: 'AvatarMenu',
  data () {
    return {
      items: [
        { title: `@${this.$auth.user.name}`, click: '' },
        { divider: true, click: '' },
        { title: 'Sign out', click: this.logout }
      ]
    }
  },
  methods: {
    logout () {
      this.$auth.logout()
    },
    usernameforAvatar () {
      return this.$auth.user.name[0].toUpperCase()
    }
  }
}
</script>

<style scoped>

</style>
