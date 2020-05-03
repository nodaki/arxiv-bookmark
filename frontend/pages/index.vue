<template>
  <div>
    <v-row align="start" justify="center">
      <v-col cols="12" sm="10" md="6">
        <div v-for="(paper, i) in papers" :key="i">
          <paper-card :paper-props="paper" class="pb-8" />
        </div>
        <!-- Infinite Loading -->
        <div>
          <infinite-loading spinner="spiral" @infinite="infiniteHandler" />
        </div>
      </v-col>
      <v-col cols="12" md="3">
        <bookmark-list :papers-props="bookmarks" style="position: fixed; width: 20vw" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import PaperCard from '../components/PaperCard'
import BookmarkList from '../components/index/BookmarkList'
export default {
  components: {
    PaperCard,
    BookmarkList
  },
  async asyncData ({ $axios }) {
    const papers = await $axios.$get('/api/v1/papers', { skip: 0, limit: 10 })
    return { papers }
  },
  data () {
    return {
      papers: [],
      limit: 10,
      skip: 10,
      bookmarks: [],
      tmp: []
    }
  },
  mounted () {
    if (this.$auth.loggedIn) {
      this.$axios.$get('/api/v1/bookmarks/my-bookmarks')
        .then((res) => {
          this.bookmarks.push(...res)
        })
    } else {
      this.tmp = []
    }
  },
  methods: {
    // Infinite loading
    infiniteHandler ($state) {
      // Get papers.
      this.$axios.$get('/api/v1/papers', { params: { skip: this.skip, limit: this.limit } })
        .then((res) => {
          if (res.length) {
            this.papers.push(...res)
            this.skip += this.limit
            $state.loaded()
          } else {
            $state.complete()
          }
        })
        .catch((e) => {
          $state.complete()
        })
    }
  }
}
</script>

<style scoped>
</style>
