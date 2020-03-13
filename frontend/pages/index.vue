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
      maxResults: 10,
      start: 0
    }
  },
  methods: {
    // Infinite loading
    infiniteHandler ($state) {
      // Get papers.
      this.$axios.$get('/api/v1/papers', { params: { start: this.start, max_results: this.max_results } })
        .then((res) => {
          this.papers.push(...res)
          this.start += this.maxResults
          $state.loaded()
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
