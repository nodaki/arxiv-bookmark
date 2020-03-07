<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      temporary
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      hide-on-scroll
      fixed
      app
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" class="d-none d-sm-flex" />
      <v-toolbar-title v-text="title" class="d-none d-sm-flex" />
      <v-spacer class="d-none d-sm-flex" />
      <search-box style="width: 20vw; min-width: 300px" />
    </v-app-bar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import SearchBox from '../components/SearchBox'
export default {
  components: {
    SearchBox
  },
  data () {
    return {
      drawer: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: ''
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Inspire',
          to: ''
        }
      ],
      title: 'ArXiv Bookmark'
    }
  }
}
</script>
