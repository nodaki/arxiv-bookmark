<template>
  <div>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="10" md="6">
        <v-card outlined>
          <v-card-title class="font-weight-bold headline pb-1">
            {{ paper.title }}
          </v-card-title>
          <v-card-text class="pb-2">
            <!-- Authors -->
            <div>
              <span class="author font-weight-light body-2">
                {{ paper.authors.join(', ') }}
              </span>
            </div>
            <!-- Affiliation -->
            <div v-if="paper.affiliation">
              <span class="font-weight-light body-2">
                {{ paper.affiliation }}
              </span>
            </div>
            <!-- calender -->
            <div>
              <span class="calender font-weight-light overline">
                {{ makeCalender(paper) }}
              </span>
            </div>
            <!-- summary -->
            <div class="body-1 font-weight-light py-4 summary">
              {{ paper.summary }}
            </div>
            <!-- category -->
            <div v-if="paper.tags" class="caption font-weight-light">
              Tag: {{ paper.tags.join(', ') }}
            </div>
            <!-- comment -->
            <div v-if="paper.arxiv_comment" class="caption font-weight-light">
              Comment: {{ paper.arxiv_comment }}
            </div>
            <!-- journal reference -->
            <div v-if="paper.journal_reference" class="caption font-weight-light">
              Ref: {{ paper.journal_reference }}
            </div>
            <!-- doi -->
            <div v-if="paper.doi" class="caption font-weight-light">
              DOI: {{ paper.doi }}
            </div>
            <!-- download -->
            <div class="caption font-weight-light">
              Download:
              <v-btn x-small text class="ml-2" :href="paper.pdf_url" target="_blank">
                <v-icon small>
                  mdi-file-pdf-outline
                </v-icon>
                PDF
              </v-btn>
              <v-btn x-small text class="ml-2" :href="paper.arxiv_url" target="_blank">
                <v-icon small>
                  mdi-open-in-new
                </v-icon>
                View in arXiv
              </v-btn>
            </div>
          </v-card-text>

          <v-divider class="mx-4" />
          <v-card-actions class="py-2">
            <v-row justify="space-around">
              <v-btn text small style="color: dimgrey">
                <v-icon>
                  mdi-bookmark-outline
                </v-icon>
                Bookmark
              </v-btn>
              <v-btn text small style="color: dimgrey">
                <v-icon>
                  mdi-comment-outline
                </v-icon>
                Comment
              </v-btn>
              <v-btn text small style="color: dimgrey">
                <v-icon>
                  mdi-share-outline
                </v-icon>
                Share
              </v-btn>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'Id',
  async asyncData ({ $axios, params }) {
    const paper = await $axios.$get(`/api/v1/papers/${params.id}`)
    return { paper }
  },
  data () {
    return {
      paper: {}
    }
  },
  methods: {
    // Parse datetime
    parseDate (date) {
      const d = new Date(date)
      return `${d.getUTCMonth() + 1}/${d.getUTCDate()}/${d.getUTCFullYear()}`
    },
    makeCalender (paper) {
      if (!paper.is_new) {
        return this.parseDate(paper.updated) + ` (v1: ${this.parseDate(paper.published)})`
      } else {
        return this.parseDate(paper.updated)
      }
    }
  }
}
</script>

<style scoped>
  .author {
    font-size: small;
  }
  .calender {
    font-size: xx-small;
  }
  .summary {
    color: black;
  }
</style>
