"""SisImports API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class SisImportsAPI(BaseCanvasAPI):
    """SisImports API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SisImportsAPI."""
        super(SisImportsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.SisImportsAPI")

    def get_sis_import_list(self, account_id, created_since=None):
        """
        Get SIS import list.

        Returns the list of SIS imports for an account
        
        Example:
          curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports' \
            -H "Authorization: Bearer <token>"
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # OPTIONAL - created_since
        """If set, only shows imports created after the specified date (use ISO8601 format)"""
        if created_since is not None:
            params["created_since"] = created_since

        self.logger.debug("GET /api/v1/accounts/{account_id}/sis_imports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/sis_imports".format(**path), data=data, params=params, all_pages=True)

    def import_sis_data(self, account_id, add_sis_stickiness=None, attachment=None, batch_mode=None, batch_mode_term_id=None, clear_sis_stickiness=None, diffing_data_set_identifier=None, diffing_remaster_data_set=None, extension=None, import_type=None, override_sis_stickiness=None):
        """
        Import SIS data.

        Import SIS data into Canvas. Must be on a root account with SIS imports
        enabled.
        
        For more information on the format that's expected here, please see the
        "SIS CSV" section in the API docs.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # OPTIONAL - import_type
        """Choose the data format for reading SIS data. With a standard Canvas
        install, this option can only be 'instructure_csv', and if unprovided,
        will be assumed to be so. Can be part of the query string."""
        if import_type is not None:
            data["import_type"] = import_type

        # OPTIONAL - attachment
        """There are two ways to post SIS import data - either via a
        multipart/form-data form-field-style attachment, or via a non-multipart
        raw post request.
        
        'attachment' is required for multipart/form-data style posts. Assumed to
        be SIS data from a file upload form field named 'attachment'.
        
        Examples:
          curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv'
        
        If you decide to do a raw post, you can skip the 'attachment' argument,
        but you will then be required to provide a suitable Content-Type header.
        You are encouraged to also provide the 'extension' argument.
        
        Examples:
          curl -H 'Content-Type: application/octet-stream' --data-binary @<filename>.zip \
              -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv&extension=zip'
        
          curl -H 'Content-Type: application/zip' --data-binary @<filename>.zip \
              -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv'
        
          curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \
              -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv'
        
          curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \
              -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv&batch_mode=1&batch_mode_term_id=15'"""
        if attachment is not None:
            data["attachment"] = attachment

        # OPTIONAL - extension
        """Recommended for raw post request style imports. This field will be used to
        distinguish between zip, xml, csv, and other file format extensions that
        would usually be provided with the filename in the multipart post request
        scenario. If not provided, this value will be inferred from the
        Content-Type, falling back to zip-file format if all else fails."""
        if extension is not None:
            data["extension"] = extension

        # OPTIONAL - batch_mode
        """If set, this SIS import will be run in batch mode, deleting any data
        previously imported via SIS that is not present in this latest import.
        See the SIS CSV Format page for details."""
        if batch_mode is not None:
            data["batch_mode"] = batch_mode

        # OPTIONAL - batch_mode_term_id
        """Limit deletions to only this term. Required if batch mode is enabled."""
        if batch_mode_term_id is not None:
            data["batch_mode_term_id"] = batch_mode_term_id

        # OPTIONAL - override_sis_stickiness
        """Many fields on records in Canvas can be marked "sticky," which means that
        when something changes in the UI apart from the SIS, that field gets
        "stuck." In this way, by default, SIS imports do not override UI changes.
        If this field is present, however, it will tell the SIS import to ignore
        "stickiness" and override all fields."""
        if override_sis_stickiness is not None:
            data["override_sis_stickiness"] = override_sis_stickiness

        # OPTIONAL - add_sis_stickiness
        """This option, if present, will process all changes as if they were UI
        changes. This means that "stickiness" will be added to changed fields.
        This option is only processed if 'override_sis_stickiness' is also provided."""
        if add_sis_stickiness is not None:
            data["add_sis_stickiness"] = add_sis_stickiness

        # OPTIONAL - clear_sis_stickiness
        """This option, if present, will clear "stickiness" from all fields touched
        by this import. Requires that 'override_sis_stickiness' is also provided.
        If 'add_sis_stickiness' is also provided, 'clear_sis_stickiness' will
        overrule the behavior of 'add_sis_stickiness'"""
        if clear_sis_stickiness is not None:
            data["clear_sis_stickiness"] = clear_sis_stickiness

        # OPTIONAL - diffing_data_set_identifier
        """If set on a CSV import, Canvas will attempt to optimize the SIS import by
        comparing this set of CSVs to the previous set that has the same data set
        identifier, and only appliying the difference between the two. See the
        SIS CSV Format documentation for more details."""
        if diffing_data_set_identifier is not None:
            data["diffing_data_set_identifier"] = diffing_data_set_identifier

        # OPTIONAL - diffing_remaster_data_set
        """If true, and diffing_data_set_identifier is sent, this SIS import will be
        part of the data set, but diffing will not be performed. See the SIS CSV
        Format documentation for details."""
        if diffing_remaster_data_set is not None:
            data["diffing_remaster_data_set"] = diffing_remaster_data_set

        self.logger.debug("POST /api/v1/accounts/{account_id}/sis_imports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/sis_imports".format(**path), data=data, params=params, single_item=True)

    def get_sis_import_status(self, id, account_id):
        """
        Get SIS import status.

        Get the status of an already created SIS import.
        
          Examples:
            curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<sis_import_id>' \
                -H "Authorization: Bearer <token>"
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/accounts/{account_id}/sis_imports/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/sis_imports/{id}".format(**path), data=data, params=params, single_item=True)

    def abort_sis_import(self, id, account_id):
        """
        Abort SIS import.

        Abort an already created but not processed or processing SIS import.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("PUT /api/v1/accounts/{account_id}/sis_imports/{id}/abort with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/sis_imports/{id}/abort".format(**path), data=data, params=params, single_item=True)

    def abort_all_pending_sis_imports(self, account_id):
        """
        Abort all pending SIS imports.

        Abort already created but not processed or processing SIS imports.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        self.logger.debug("PUT /api/v1/accounts/{account_id}/sis_imports/abort_all_pending with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/sis_imports/abort_all_pending".format(**path), data=data, params=params)


class Sisimport(BaseModel):
    """Sisimport Model."""

    def __init__(self, ended_at=None, diffed_against_import_id=None, workflow_state=None, batch_mode=None, created_at=None, batch_mode_term_id=None, clear_sis_stickiness=None, updated_at=None, override_sis_stickiness=None, processing_errors=None, add_sis_stickiness=None, diffing_data_set_identifier=None, processing_warnings=None, progress=None, data=None, id=None):
        """Init method for Sisimport class."""
        self._ended_at = ended_at
        self._diffed_against_import_id = diffed_against_import_id
        self._workflow_state = workflow_state
        self._batch_mode = batch_mode
        self._created_at = created_at
        self._batch_mode_term_id = batch_mode_term_id
        self._clear_sis_stickiness = clear_sis_stickiness
        self._updated_at = updated_at
        self._override_sis_stickiness = override_sis_stickiness
        self._processing_errors = processing_errors
        self._add_sis_stickiness = add_sis_stickiness
        self._diffing_data_set_identifier = diffing_data_set_identifier
        self._processing_warnings = processing_warnings
        self._progress = progress
        self._data = data
        self._id = id

        self.logger = logging.getLogger('pycanvas.Sisimport')

    @property
    def ended_at(self):
        """The date the SIS import finished. Returns null if not finished."""
        return self._ended_at

    @ended_at.setter
    def ended_at(self, value):
        """Setter for ended_at property."""
        self.logger.warn("Setting values on ended_at will NOT update the remote Canvas instance.")
        self._ended_at = value

    @property
    def diffed_against_import_id(self):
        """The ID of the SIS Import that this import was diffed against."""
        return self._diffed_against_import_id

    @diffed_against_import_id.setter
    def diffed_against_import_id(self, value):
        """Setter for diffed_against_import_id property."""
        self.logger.warn("Setting values on diffed_against_import_id will NOT update the remote Canvas instance.")
        self._diffed_against_import_id = value

    @property
    def workflow_state(self):
        """The current state of the SIS import. - 'created': The SIS import has been created.
 - 'importing': The SIS import is currently processing.
 - 'cleanup_batch': The SIS import is currently cleaning up courses, sections, and enrollments not included in the batch for batch_mode imports.
 - 'imported': The SIS import has completed successfully.
 - 'imported_with_messages': The SIS import completed with errors or warnings.
 - 'failed_with_messages': The SIS import failed with errors.
 - 'failed': The SIS import failed."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def batch_mode(self):
        """Whether the import was run in batch mode."""
        return self._batch_mode

    @batch_mode.setter
    def batch_mode(self, value):
        """Setter for batch_mode property."""
        self.logger.warn("Setting values on batch_mode will NOT update the remote Canvas instance.")
        self._batch_mode = value

    @property
    def created_at(self):
        """The date the SIS import was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def batch_mode_term_id(self):
        """The term the batch was limited to."""
        return self._batch_mode_term_id

    @batch_mode_term_id.setter
    def batch_mode_term_id(self, value):
        """Setter for batch_mode_term_id property."""
        self.logger.warn("Setting values on batch_mode_term_id will NOT update the remote Canvas instance.")
        self._batch_mode_term_id = value

    @property
    def clear_sis_stickiness(self):
        """Whether stickiness was cleared."""
        return self._clear_sis_stickiness

    @clear_sis_stickiness.setter
    def clear_sis_stickiness(self, value):
        """Setter for clear_sis_stickiness property."""
        self.logger.warn("Setting values on clear_sis_stickiness will NOT update the remote Canvas instance.")
        self._clear_sis_stickiness = value

    @property
    def updated_at(self):
        """The date the SIS import was last updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def override_sis_stickiness(self):
        """Whether UI changes were overridden."""
        return self._override_sis_stickiness

    @override_sis_stickiness.setter
    def override_sis_stickiness(self, value):
        """Setter for override_sis_stickiness property."""
        self.logger.warn("Setting values on override_sis_stickiness will NOT update the remote Canvas instance.")
        self._override_sis_stickiness = value

    @property
    def processing_errors(self):
        """An array of CSV_file/error_message pairs."""
        return self._processing_errors

    @processing_errors.setter
    def processing_errors(self, value):
        """Setter for processing_errors property."""
        self.logger.warn("Setting values on processing_errors will NOT update the remote Canvas instance.")
        self._processing_errors = value

    @property
    def add_sis_stickiness(self):
        """Whether stickiness was added to the batch changes."""
        return self._add_sis_stickiness

    @add_sis_stickiness.setter
    def add_sis_stickiness(self, value):
        """Setter for add_sis_stickiness property."""
        self.logger.warn("Setting values on add_sis_stickiness will NOT update the remote Canvas instance.")
        self._add_sis_stickiness = value

    @property
    def diffing_data_set_identifier(self):
        """The identifier of the data set that this SIS batch diffs against."""
        return self._diffing_data_set_identifier

    @diffing_data_set_identifier.setter
    def diffing_data_set_identifier(self, value):
        """Setter for diffing_data_set_identifier property."""
        self.logger.warn("Setting values on diffing_data_set_identifier will NOT update the remote Canvas instance.")
        self._diffing_data_set_identifier = value

    @property
    def processing_warnings(self):
        """Only imports that are complete will get this data. An array of CSV_file/warning_message pairs."""
        return self._processing_warnings

    @processing_warnings.setter
    def processing_warnings(self, value):
        """Setter for processing_warnings property."""
        self.logger.warn("Setting values on processing_warnings will NOT update the remote Canvas instance.")
        self._processing_warnings = value

    @property
    def progress(self):
        """The progress of the SIS import. The progress will reset when using batch_mode and have a different progress for the cleanup stage."""
        return self._progress

    @progress.setter
    def progress(self, value):
        """Setter for progress property."""
        self.logger.warn("Setting values on progress will NOT update the remote Canvas instance.")
        self._progress = value

    @property
    def data(self):
        """data."""
        return self._data

    @data.setter
    def data(self, value):
        """Setter for data property."""
        self.logger.warn("Setting values on data will NOT update the remote Canvas instance.")
        self._data = value

    @property
    def id(self):
        """The unique identifier for the SIS import."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Sisimportcounts(BaseModel):
    """Sisimportcounts Model."""

    def __init__(self, terms=None, users=None, batch_enrollments_deleted=None, grade_publishing_results=None, abstract_courses=None, group_memberships=None, courses=None, batch_sections_deleted=None, accounts=None, xlists=None, groups=None, enrollments=None, batch_courses_deleted=None, sections=None):
        """Init method for Sisimportcounts class."""
        self._terms = terms
        self._users = users
        self._batch_enrollments_deleted = batch_enrollments_deleted
        self._grade_publishing_results = grade_publishing_results
        self._abstract_courses = abstract_courses
        self._group_memberships = group_memberships
        self._courses = courses
        self._batch_sections_deleted = batch_sections_deleted
        self._accounts = accounts
        self._xlists = xlists
        self._groups = groups
        self._enrollments = enrollments
        self._batch_courses_deleted = batch_courses_deleted
        self._sections = sections

        self.logger = logging.getLogger('pycanvas.Sisimportcounts')

    @property
    def terms(self):
        """terms."""
        return self._terms

    @terms.setter
    def terms(self, value):
        """Setter for terms property."""
        self.logger.warn("Setting values on terms will NOT update the remote Canvas instance.")
        self._terms = value

    @property
    def users(self):
        """users."""
        return self._users

    @users.setter
    def users(self, value):
        """Setter for users property."""
        self.logger.warn("Setting values on users will NOT update the remote Canvas instance.")
        self._users = value

    @property
    def batch_enrollments_deleted(self):
        """the number of enrollments that were removed because they were not included in the batch for batch_mode imports. Only included if enrollments were deleted."""
        return self._batch_enrollments_deleted

    @batch_enrollments_deleted.setter
    def batch_enrollments_deleted(self, value):
        """Setter for batch_enrollments_deleted property."""
        self.logger.warn("Setting values on batch_enrollments_deleted will NOT update the remote Canvas instance.")
        self._batch_enrollments_deleted = value

    @property
    def grade_publishing_results(self):
        """grade_publishing_results."""
        return self._grade_publishing_results

    @grade_publishing_results.setter
    def grade_publishing_results(self, value):
        """Setter for grade_publishing_results property."""
        self.logger.warn("Setting values on grade_publishing_results will NOT update the remote Canvas instance.")
        self._grade_publishing_results = value

    @property
    def abstract_courses(self):
        """abstract_courses."""
        return self._abstract_courses

    @abstract_courses.setter
    def abstract_courses(self, value):
        """Setter for abstract_courses property."""
        self.logger.warn("Setting values on abstract_courses will NOT update the remote Canvas instance.")
        self._abstract_courses = value

    @property
    def group_memberships(self):
        """group_memberships."""
        return self._group_memberships

    @group_memberships.setter
    def group_memberships(self, value):
        """Setter for group_memberships property."""
        self.logger.warn("Setting values on group_memberships will NOT update the remote Canvas instance.")
        self._group_memberships = value

    @property
    def courses(self):
        """courses."""
        return self._courses

    @courses.setter
    def courses(self, value):
        """Setter for courses property."""
        self.logger.warn("Setting values on courses will NOT update the remote Canvas instance.")
        self._courses = value

    @property
    def batch_sections_deleted(self):
        """the number of sections that were removed because they were not included in the batch for batch_mode imports. Only included if sections were deleted."""
        return self._batch_sections_deleted

    @batch_sections_deleted.setter
    def batch_sections_deleted(self, value):
        """Setter for batch_sections_deleted property."""
        self.logger.warn("Setting values on batch_sections_deleted will NOT update the remote Canvas instance.")
        self._batch_sections_deleted = value

    @property
    def accounts(self):
        """accounts."""
        return self._accounts

    @accounts.setter
    def accounts(self, value):
        """Setter for accounts property."""
        self.logger.warn("Setting values on accounts will NOT update the remote Canvas instance.")
        self._accounts = value

    @property
    def xlists(self):
        """xlists."""
        return self._xlists

    @xlists.setter
    def xlists(self, value):
        """Setter for xlists property."""
        self.logger.warn("Setting values on xlists will NOT update the remote Canvas instance.")
        self._xlists = value

    @property
    def groups(self):
        """groups."""
        return self._groups

    @groups.setter
    def groups(self, value):
        """Setter for groups property."""
        self.logger.warn("Setting values on groups will NOT update the remote Canvas instance.")
        self._groups = value

    @property
    def enrollments(self):
        """enrollments."""
        return self._enrollments

    @enrollments.setter
    def enrollments(self, value):
        """Setter for enrollments property."""
        self.logger.warn("Setting values on enrollments will NOT update the remote Canvas instance.")
        self._enrollments = value

    @property
    def batch_courses_deleted(self):
        """the number of courses that were removed because they were not included in the batch for batch_mode imports. Only included if courses were deleted."""
        return self._batch_courses_deleted

    @batch_courses_deleted.setter
    def batch_courses_deleted(self, value):
        """Setter for batch_courses_deleted property."""
        self.logger.warn("Setting values on batch_courses_deleted will NOT update the remote Canvas instance.")
        self._batch_courses_deleted = value

    @property
    def sections(self):
        """sections."""
        return self._sections

    @sections.setter
    def sections(self, value):
        """Setter for sections property."""
        self.logger.warn("Setting values on sections will NOT update the remote Canvas instance.")
        self._sections = value


class Sisimportdata(BaseModel):
    """Sisimportdata Model."""

    def __init__(self, import_type=None, counts=None, supplied_batches=None):
        """Init method for Sisimportdata class."""
        self._import_type = import_type
        self._counts = counts
        self._supplied_batches = supplied_batches

        self.logger = logging.getLogger('pycanvas.Sisimportdata')

    @property
    def import_type(self):
        """The type of SIS import."""
        return self._import_type

    @import_type.setter
    def import_type(self, value):
        """Setter for import_type property."""
        self.logger.warn("Setting values on import_type will NOT update the remote Canvas instance.")
        self._import_type = value

    @property
    def counts(self):
        """The number of rows processed for each type of import."""
        return self._counts

    @counts.setter
    def counts(self, value):
        """Setter for counts property."""
        self.logger.warn("Setting values on counts will NOT update the remote Canvas instance.")
        self._counts = value

    @property
    def supplied_batches(self):
        """Which files were included in the SIS import."""
        return self._supplied_batches

    @supplied_batches.setter
    def supplied_batches(self, value):
        """Setter for supplied_batches property."""
        self.logger.warn("Setting values on supplied_batches will NOT update the remote Canvas instance.")
        self._supplied_batches = value

