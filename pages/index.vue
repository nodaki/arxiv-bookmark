<template>
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
          <v-clamp class="mt-2" autoresize :max-lines="clampMaxLines">
            {{ paper.summary }}
          </v-clamp>
          <div class="mt-3">
            <!-- New or update -->
            <span class="font-weight-bold">
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
            >
              {{ category.$.term }}
            </v-chip>
          </div>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
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
      papers: [
        {
          title: '',
          id: '',
          published: '',
          updated: '',
          summary: '',
          authors: [],
          link: '',
          categories: [],
          comment: '',
          conferences: [],
          isNew: true
        }
      ]
    }
  },
  created () {
    const url = 'https://export.arxiv.org/api/query?search_query=cat:cs.CV&sortBy=lastUpdatedDate&sortOrder=descending'
    this.papers = this.getPapers(url)
  },
  methods: {
    getPapers (url) {
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
      // Parse arxiv API response.
      parser.parseURL(url).then(function (feed) {
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
      })
      return papers
    }
  }
}
</script>
