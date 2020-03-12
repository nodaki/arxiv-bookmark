<template>
  <div>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-text class="pb-0">
            <v-form>
              <p class="mb-0">
                Username
              </p>
              <v-text-field v-model="form.name" outlined dense name="name" type="text" />
              <p class="mb-0">
                Email
              </p>
              <v-text-field v-model="form.email" outlined dense name="email" type="text" />
              <p class="mb-0">
                Password
              </p>
              <v-text-field
                id="password"
                v-model="form.password"
                outlined
                dense
                name="password"
                type="password"
              />
            </v-form>
          </v-card-text>
          <v-card-actions class="pl-4 pr-4">
            <v-btn class="mb-2" color="success" block @click="register">
              Register
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data () {
    return {
      form: {
        name: '',
        email: '',
        password: ''
      }
    }
  },
  methods: {
    async register () {
      try {
        // Registration
        await this.$axios.$post('/api/v1/users/open', this.form)
        // Sign in
        await this.$auth.loginWith('local', {
          data: `username=${this.form.email}&password=${this.form.password}`
        })
      } catch (e) {
        // eslint-disable-next-line no-console
        console.log(e)
      }
    }
  }
}
</script>

<style scoped>

</style>
