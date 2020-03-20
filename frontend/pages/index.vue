<template>
  <div>
    <v-row v-for="(paper, i) in papers" :key="i" align="center" justify="center">
      <v-col cols="12" sm="10" md="6">
        <paper-card :paper="paper" />
      </v-col>
    </v-row>
    <!-- Infinite Loading -->
    <div>
      <infinite-loading spinner="spiral" @infinite="infiniteHandler" />
    </div>
  </div>
</template>

<script>
import PaperCard from '../components/PaperCard'
export default {
  components: {
    PaperCard
  },
  data () {
    return {
      papers: [],
      limit: 10,
      skip: 0
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
