<template>
  <div>
    <v-row v-for="(paper, i) in papers" :key="i">
      <v-col>
        <v-hover v-slot:default="{ hover }">
          <v-card :elevation="hover ? 5 : 2" :ripple="false" @click="openDialog(paper)">
            <v-card-title class="mb-2">
              {{ paper.title }}
            </v-card-title>
            <v-card-text>
              <!-- Authors -->
              <div>
                <v-chip class="caption mr-1 mb-2" outlined x-small label color="brown lighten-1">
                  <v-icon left small>
                    mdi-account-circle-outline
                  </v-icon>
                  {{ paper.authors[0] }}
                </v-chip>
                <v-chip
                  v-for="(author, j) in paper.authors.slice(1)"
                  :key="j"
                  class="caption mr-1 mb-2 hidden-xs-only"
                  outlined
                  x-small
                  label
                  color="brown lighten-1"
                >
                  <v-icon left small>
                    mdi-account-circle-outline
                  </v-icon>
                  {{ author }}
                </v-chip>
              </div>
              <!-- Summary -->
              <v-clamp :max-lines="clampMaxLines" class="body mt-2" autoresize>
                {{ paper.summary }}
              </v-clamp>
              <div class="mt-4 ml-3 mr-3">
                <v-row class="mt-1">
                  <!-- New or update -->
                  <span class="font-weight-bold mr-1 mb-1">
                    <v-chip v-if="paper.is_new" label color="teal lighten-1" text-color="white" small>
                      New
                    </v-chip>
                    <v-chip v-else label color="teal lighten-3" text-color="white" small>
                      Updated
                    </v-chip>
                  </span>
                  <!-- Conference -->
                  <span class="font-weight-bold">
                    <v-chip
                      v-for="(conference, j) in paper.conferences"
                      :key="j"
                      label
                      color="amber lighten-1"
                      text-color="white"
                      small
                      class="mr-1 mb-1"
                    >
                      {{ conference }}
                    </v-chip>
                  </span>
                  <!-- Categories -->
                  <v-chip
                    v-for="(category, k) in paper.tags"
                    :key="k"
                    small
                    label
                    class="mr-1 mb-1"
                    color="grey lighten-2"
                    text-color="grey darken-2"
                  >
                    {{ category }}
                  </v-chip>
                  <v-spacer />
                  <!-- Calendar -->
                  <div class="hidden-xs-only">
                    <v-icon x-small>
                      calendar_today
                    </v-icon>
                    <span class="caption">
                      {{ parseDate(paper.updated) }}
                    </span>
                    <span v-if="!paper.is_new" class="caption">
                      (v1: {{ parseDate(paper.published) }})
                    </span>
                  </div>
                </v-row>
                <v-row>
                  <!-- Calendar -->
                  <div class="d-flex d-sm-none mt-1">
                    <v-icon x-small>
                      calendar_today
                    </v-icon>
                    <span class="caption">
                      {{ parseDate(paper.updated) }}
                    </span>
                    <span v-if="!paper.is_new" class="caption">
                      (v1: {{ parseDate(paper.published) }})
                    </span>
                  </div>
                </v-row>
              </div>
            </v-card-text>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>
    <!-- Dialog -->
    <v-row>
      <v-col>
        <v-dialog v-model="dialog" max-width="800" scrollable>
          <v-card>
            <v-card-text id="scroll-target">
              <!-- Title -->
              <div class="title text--primary pb-3 pt-5">
                {{ dialogContent.title }}
              </div>
              <!-- Authors -->
              <div class="pb-1">
                <v-chip
                  v-for="(author, j) in dialogContent.authors"
                  :key="j"
                  class="caption mr-1 mb-2"
                  outlined
                  x-small
                  label
                  color="brown lighten-1"
                >
                  <v-icon left x-small>
                    mdi-account-circle-outline
                  </v-icon>
                  {{ author }}
                </v-chip>
              </div>
              <div class="pb-2">
                <!-- Calendar -->
                <v-icon x-small>
                  calendar_today
                </v-icon>
                <span class="caption">
                  {{ parseDate(dialogContent.updated) }}
                </span>
                <span v-if="!dialogContent.is_new" class="caption">
                  (v1: {{ parseDate(dialogContent.published) }})
                </span>
              </div>
              <!-- Abstract -->
              <div class="text-center text--primary pb-1">
                Abstract
              </div>
              <!-- Abstract -->
              <div class="text--primary">
                {{ dialogContent.summary }}
              </div>
              <!-- Comment -->
              <div class="caption pt-2">
                Comment: {{ dialogContent.arxiv_comment }}
              </div>
            </v-card-text>
            <v-divider />
            <!-- Actions -->
            <v-card-actions>
              <div class="flex-grow-1" />
              <v-btn color="primary" text @click="dialog = false">
                Close
              </v-btn>
              <v-btn :href="dialogContent.pdf_url" color="primary" target="_blank">
                Full Text
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
    <!-- Infinite Loading -->
    <div>
      <infinite-loading spinner="spiral" @infinite="infiniteHandler" />
    </div>
  </div>
</template>

<script>
import VClamp from 'vue-clamp'
export default {
  components: {
    VClamp
  },
  middleware: 'auth',
  data () {
    return {
      papers: [],
      maxResults: 10,
      start: 0,
      clampMaxLines: 3,
      dialog: false,
      dialogContent: {}
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
    },
    // Parse datetime
    parseDate (date) {
      const d = new Date(date)
      return `${d.getUTCFullYear()}/${d.getUTCMonth() + 1}/${d.getUTCDay()}`
    },
    openDialog (paper) {
      this.dialogContent = paper
      this.dialog = true
      // Set scroll top to 0
      this.$nextTick(() => {
        const i = document.getElementById('scroll-target')
        i.attributes[1].ownerElement.scrollTop = 0
      })
    }
  }
}
</script>

<style scoped>
</style>
