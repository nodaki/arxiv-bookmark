<template>
  <div>
    <v-card outlined>
      <v-card-title class="font-weight-bold pb-1">
        {{ paper.title }}
      </v-card-title>
      <v-card-text class="pb-2">
        <!-- Authors -->
        <div>
          <span class="author font-weight-light">
            {{ paper.authors.join(', ') }}
          </span>
        </div>
        <!-- calender -->
        <div>
          <span class="calender font-weight-light">
            {{ makeCalender(paper) }}
          </span>
        </div>
        <!-- Summary -->
        <v-clamp :max-lines="clampMaxLines" class="body" autoresize>
          {{ paper.summary }}
        </v-clamp>
        <div class="mt-3 ml-3 mr-3">
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
          </v-row>
        </div>
      </v-card-text>
      <v-divider class="mx-4" />
      <v-card-actions class="py-1">
        <v-row justify="space-around">
          <v-btn icon>
            <v-icon>
              mdi-bookmark-outline
            </v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>
              mdi-comment-outline
            </v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>
              mdi-share-outline
            </v-icon>
          </v-btn>
        </v-row>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import VClamp from 'vue-clamp'
export default {
  name: 'PaperCard',
  components: {
    VClamp
  },
  props: {
    paper: {
      type: Object,
      default () {
        return {
          title: '',
          authors: [],
          summary: '',
          conferences: [],
          tags: [],
          published: '',
          updated: '',
          is_new: false
        }
      }
    }
  },
  data () {
    return {
      clampMaxLines: 6
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
</style>
