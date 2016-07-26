import subprocess
import os
import shutil
import multiprocessing

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
p = lambda a: os.path.join(BASE_PATH, a)

specs = [
        # 'account_authentication_services.json',
        # 'account_domain_lookups.json',
        # 'account_notifications.json',
        # 'account_reports.json',
        # 'accounts.json',
        # 'admins.json',
        # 'announcement_external_feeds.json',
        # 'appointment_groups.json',
        # 'assignment_groups.json',
        # 'assignments.json',
        # 'authentications_log.json',
        # 'calendar_events.json',
        # 'collaborations.json',
        # 'comm_messages.json',
        # 'communication_channels.json',
        # 'conferences.json',
        # 'content_exports.json',
        # 'content_migrations.json',
        # 'conversations.json',
        # 'course_audit_log.json',
        # 'course_quiz_extensions.json',
        # 'courses.json',
        # 'custom_gradebook_columns.json',
        # 'discussion_topics.json',
        # 'document_previews.json',
        # 'enrollment_terms.json',
        # 'enrollments.json',
        # 'external_tools.json',
        # 'favorites.json',
        # 'feature_flags.json',
        # 'files.json',
        # 'grade_change_log.json',
        # 'gradebook_history.json',
        # 'grading_periods.json',
        # 'grading_standards.json',
        # 'group_categories.json',
        # 'groups.json',
        # 'live_assessments.json',
        # 'logins.json',
        # 'modules.json',
        # 'notification_preferences.json',
        # 'outcome_groups.json',
        # 'outcome_results.json',
        # 'outcomes.json',
        # 'pages.json',
        # 'poll_choices.json',
        # 'poll_sessions.json',
        # 'poll_submissions.json',
        # 'polls.json',
        # 'progress.json',
        # 'quiz_assignment_overrides.json',
        # 'quiz_extensions.json',
        # 'quiz_ip_filters.json',
        # 'quiz_question_groups.json',
        # 'quiz_questions.json',
        # 'quiz_reports.json',
        # 'quiz_statistics.json',
        # 'quiz_submission_events.json',
        # 'quiz_submission_files.json',
        # 'quiz_submission_questions.json',
        # 'quiz_submission_user_list.json',
        # 'quiz_submissions.json',
        # 'quizzes.json',
        # 'roles.json',
        # 'search.json',
        # 'sections.json',
        # 'services.json',
        # 'sis_imports.json',
        # 'submission_comments.json',
        # 'submissions.json',
        # 'tabs.json',
        # 'user_observees.json',
        'users.json',
        # 'api-docs.json',
    ]


def process_swagger_def(d):
    with open(d[1], 'w+') as f:
        subprocess.call(d[0], stderr=f, stdout=f)



def main():
    # Create a log dir
    try:
        os.mkdir(p('logs'))
    except OSError:
        shutil.rmtree(p('logs'))
        os.mkdir(p('logs'))

    if os.path.exists(p('apis')):
        shutil.rmtree(p('apis'))
        os.mkdir(p('apis'))
        with open(p('apis/__init__.py'), 'w+') as f:
            f.write('# __init__.py')

    pool = multiprocessing.Pool(processes=4)
    data = []
    results = {}

    for spec in os.listdir(p('specs')):
        name = spec[:spec.find('.json')]
        # setup logging
        os.mkdir(os.path.join(BASE_PATH, 'logs/{}'.format(name)))
        output_path = os.path.join(BASE_PATH, './logs/{name}/{name}.log'.format(name=name))
        subprocess_args = ['java', '-jar', 'swagger-codegen-cli.jar', 'generate', '-i', p('specs/{}'.format(spec)), '-l', 'python', '-o', 'apis/{}'.format(name), '-t', p('templates')]
        data.append((subprocess_args, output_path))

    it = pool.map(process_swagger_def, data)

    pool.close()
    pool.join()

    for api in os.listdir(p('apis')):
        if api == '__init__.py':
            continue
        if os.path.exists(p('apis/{}/__init__.py'.format(api))):
            continue
        destination = p('apis/{}'.format(api))
        source = p('apis/{}/swagger_client'.format(api))
        temporary = p('apis/{}_temp'.format(api))
        shutil.copytree(source, temporary)
        shutil.rmtree(destination)
        os.rename(temporary, destination)
        if not os.path.exists(p('apis/configuration.py')):
            shutil.copyfile(os.path.join(destination, 'configuration.py'), p('apis/configuration.py'))
        if not os.path.exists(p('apis/rest.py')):
            shutil.copyfile(os.path.join(destination, 'rest.py'), p('apis/rest.py'))
        os.remove(os.path.join(destination, 'configuration.py'))
        os.remove(os.path.join(destination, 'rest.py'))


if __name__ == '__main__':
    main()