<template>
  <div>
    <v-row>
      <v-col v-for="(paper, i) in papers" :key="i" xs="12" sm="12">
        <v-card>
          <v-card-title class="mb-2">
            {{ paper.title }}
          </v-card-title>
          <v-card-text>
            <!-- Authors -->
            <div>
              <v-chip
                v-for="(author, j) in paper.authors"
                :key="j"
                class="caption mr-1 mb-2"
                outlined
                small
                label
                color="brown lighten-1"
              >
                <v-icon left small>
                  mdi-account-circle-outline
                </v-icon>
                {{ author.name[0] }}
              </v-chip>
            </div>
            <!-- Summary -->
            <v-clamp class="body mt-2" autoresize :max-lines="clampMaxLines">
              {{ paper.summary }}
            </v-clamp>
            <div class="mt-4 ml-3 mr-3">
              <v-row class="mt-1">
                <!-- New or update -->
                <span class="font-weight-bold mr-1">
                  <v-chip v-if="paper.isNew" label color="teal lighten-1" text-color="white" small>
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
                    class="mr-1"
                    @click="setComment(conference)"
                  >
                    {{ conference }}
                  </v-chip>
                </span>
                <!-- Categories -->
                <v-chip
                  v-for="(category, k) in paper.categories"
                  :key="k"
                  small
                  label
                  class="mr-1"
                  color="grey lighten-2"
                  text-color="grey darken-2"
                  @click="setCategory(category.$.term)"
                >
                  {{ category.$.term }}
                </v-chip>
                <v-spacer />
                <!-- Calendar -->
                <div>
                  <v-icon small>
                    calendar_today
                  </v-icon>
                  <span>
                    {{ paper.updated.year }}/{{ paper.updated.month }}/{{ paper.updated.day }}
                  </span>
                  <span v-if="!paper.isNew" class="body-2">
                    (v1: {{ paper.published.year }}/{{ paper.published.month }}/{{ paper.published.day }})
                  </span>
                </div>
              </v-row>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <div>
      <infinite-loading ref="infiniteLoading" spinner="spiral" @infinite="infiniteHandler" />
    </div>
  </div>
</template>

<script>
import VClamp from 'vue-clamp'
export default {
  components: {
    VClamp
  },
  data () {
    return {
      clampMaxLines: 3,
      page: 0,
      maxResults: 10,
      cat: 'cs.CV',
      comment: '',
      baseUrl: 'https://export.arxiv.org/api/query?sortBy=lastUpdatedDate&sortOrder=descending&search_query=',
      papers: []
    }
  },
  methods: {
    async asyncGetPapers (url) {
      const Parser = require('rss-parser')
      const options = {
        customFields: {
          item: [
            ['published', 'published'],
            ['updated', 'updated'],
            ['summary', 'summary'],
            ['author', 'authors', { keepArray: true }],
            ['category', 'categories', { keepArray: true }],
            ['arxiv:comment', 'comment']
          ]
        }
      }
      const parser = new Parser(options)
      const papers = []
      const parseDate = (date) => {
        return {
          year: date.getUTCFullYear(),
          month: date.getUTCMonth() + 1,
          day: date.getUTCDate()
        }
      }
      const feed = await parser.parseURL(url)
      feed.items.forEach(function (entry) {
        const pubDate = new Date(entry.published)
        const updatedDate = new Date(entry.updated)
        // Check whether new or update
        const isNew = entry.published === entry.updated
        let comment
        if (entry.comment) {
          comment = entry.comment._
        } else {
          comment = ''
        }
        // Get conference info from comment.
        const searchConferences = ['CVPR', 'ICCV', 'ACCV', 'ECCV', 'NIPS', 'NeurIPS', 'SIGGRAPH', 'AAAI', 'ICML', 'IJCAI']
        const conferences = []
        searchConferences.forEach(function (conference) {
          if (comment.includes(conference)) {
            conferences.push(conference)
          }
        })
        papers.push({
          title: entry.title,
          id: entry.id,
          published: parseDate(pubDate),
          updated: parseDate(updatedDate),
          summary: entry.summary,
          authors: entry.authors,
          categories: entry.categories,
          comment,
          conferences,
          isNew
        })
      })
      return papers
    },
    async infiniteHandler ($state) {
      // Infinite loading
      if (this.loading) { return }
      try {
        this.loading = false
        const start = `&start=${this.page * this.maxResults}`
        const andOperator = '+AND+'
        const cat = `cat:${this.cat}`
        let searchQuery
        if (this.comment) {
          searchQuery = cat + andOperator + `co:${this.comment}`
        } else {
          searchQuery = cat
        }
        const url = this.baseUrl + searchQuery + start + `&max_results=${this.maxResults}`
        const papers = await this.asyncGetPapers(url)
        this.papers.push(...papers)
        this.page += 1
        $state.loaded()
      } catch (e) {
        $state.complete()
      } finally {
        this.loading = false
      }
    },
    resetInfiniteLoading () {
      this.page = 0
      this.papers = []
      // Reset infinite loading
      this.$refs.infiniteLoading.stateChanger.reset()
    },
    setCategory (cat) {
      this.cat = cat
      this.resetInfiniteLoading()
    },
    setComment (comment) {
      this.comment = comment
      this.resetInfiniteLoading()
    }
  }
}
</script>
