<template>
  <v-app>
    <v-app-bar fixed app elevation="2" dense color="white">
      <v-container>
        <v-row align="center">
          <v-toolbar-title class="d-none d-sm-flex" v-text="title" />
          <v-spacer />
          <!-- After login -->
          <div v-if="this.$auth.loggedIn">
            <avatar-menu />
          </div>
          <!-- Before login -->
          <div v-else>
            <v-btn text to="/login">
              Sign in
            </v-btn>
            <v-btn text outlined to="/register">
              Register
            </v-btn>
          </div>
        </v-row>
      </v-container>
    </v-app-bar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import AvatarMenu from '../components/AvatarMenu'
export default {
  components: {
    AvatarMenu
  },
  data () {
    return {
      title: 'ArXiv Bookmark'
    }
  }
}
</script>
